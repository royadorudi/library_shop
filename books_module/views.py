import mimetypes
import os
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from writers_module.models import Writers, Translators
from .forms import CommentsModelForm
from .models import BookCategory, Books, BookComments


class BookCategoriesView(ListView):
    model = BookCategory
    template_name = 'books_module/books_category_page.html'
    context_object_name = 'book_categories'
    paginate_by = 6

    def get_queryset(self):
        query = super(BookCategoriesView, self).get_queryset()
        query = query.filter(is_active=True, is_delete=False).all()
        return query


class BookCategoriesDetailView(DetailView):
    model = BookCategory
    template_name = 'books_module/categories_detail_page.html'
    context_object_name = 'books'


class BookDetailView(DetailView):
    model = Books
    template_name = 'books_module/book_detail_page.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data()
        context['bookmark_check'] = False
        pk = self.kwargs.get('pk')
        url_title = self.kwargs.get('str')
        current_writer = Writers.objects.filter(book__id=pk, book__url_title=url_title).first()
        current_translator = Translators.objects.filter(book__id=pk, book__url_title=url_title).first()
        context['current_writer'] = current_writer
        context['current_translator'] = current_translator
        if Books.objects.filter(bookmarks__id=self.request.user.id, id=pk, url_title=url_title).exists():
            context['bookmark_check'] = True
        return context


class BooksListView(ListView):
    model = Books
    template_name = 'books_module/allBooks_list_page.html'
    context_object_name = 'all_books'
    paginate_by = 6

    def get_queryset(self):
        query = super(BooksListView, self).get_queryset()
        query = query.filter(is_active=True, is_delete=False,
                             category__is_active=True, category__is_delete=False).all().order_by('-submit_date')
        return query


def add_to_bookmark(request, pk):
    user_id = request.user.id
    has_bookmarked: Books = Books.objects.filter(id=pk, bookmarks__id=user_id).first()
    if has_bookmarked is None:
        new_bookmark = Books.objects.filter(id=pk).first()
        new_bookmark.bookmarks.add(user_id)
        new_bookmark.save()
    messages.success(request, 'بوک مارک شد!')
    return redirect(request.GET.get('next'))


def remove_from_bookmark(request: HttpRequest, pk):
    user_id = request.user.id
    has_bookmarked: Books = Books.objects.filter(id=pk, bookmarks__id=user_id).first()
    if has_bookmarked is not None:
        has_bookmarked.bookmarks.remove(user_id)
        has_bookmarked.save()
    messages.error(request, 'بوک مارکِت پاک شد!')
    return redirect(request.GET.get('next'))


def download_file(request, filename=''):
    if filename != '':
        # Define Django project base directory
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Define the full file path
        filepath = BASE_DIR + '/uploads/files/books/' + filename
        # Open the file for reading content
        path = open(filepath, 'rb')
        # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response = HttpResponse(path, content_type=mime_type)
        # Set the HTTP header for sending to browser
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        # Return the response value
        return response
    else:
        return render(request, 'books_module/book_detail_page.html')


def comments_list_and_form(request: HttpRequest, book_id, book_name, parent_id):
    all_comments = BookComments.objects.filter(book__id=book_id, book__title=book_name, parent_id=None).order_by('-submit_date').all()
    current_book = Books.objects.filter(id=book_id, title=book_name).first()
    current_user = request.user
    comments_count = BookComments.objects.filter(book__id=book_id, book__title=book_name).count()
    if request.method == 'POST':
        comment_form = CommentsModelForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.cleaned_data.get('comment')
            if parent_id == 0:
                reply_checker = None
            else:
                reply_checker = parent_id
            new_comment = BookComments(
                book=current_book,
                user=current_user,
                comment=user_comment,
                parent_id=reply_checker
            )
            new_comment.save()
            return redirect(reverse('book_comments_page', kwargs={
                'book_id': book_id,
                'book_name': book_name,
                'parent_id': parent_id
            }))
    else:
        comment_form = CommentsModelForm()

    return render(request, 'books_module/bookComments.html', {
        'all_comments': all_comments,
        'comment_form': comment_form,
        'current_book': current_book,
        'comments_count': comments_count,
        'current_user': current_user,
    })


def delete_comment(request: HttpRequest, comment_id):
    user_id = request.user.id
    selected_comment = BookComments.objects.filter(id=comment_id, user_id=user_id).first()
    if selected_comment is not None:
        selected_comment.delete()
    return redirect(request.GET.get('next'))





