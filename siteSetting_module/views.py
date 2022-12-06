from django.http import HttpRequest
from django.shortcuts import render
from django.db.models import Q
from books_module.models import Books
from django.core.paginator import Paginator


def search_box(request: HttpRequest):
    if request.GET:
        searched = request.GET.get('searched')
        books = Books.objects.filter(Q(title__contains=searched) | Q(writer__contains=searched) |
                                     Q(translator__contains=searched)).all()
        page = request.GET.get('page')
        paginator = Paginator(list(books), per_page=6)
        page_obj = paginator.get_page(page)
        return render(request, 'siteSetting_module/search_result_page.html', {
            'books': books,
            'searched': searched,
            'page_obj': page_obj
        })
    else:
        return render(request, 'siteSetting_module/search_result_page.html')
