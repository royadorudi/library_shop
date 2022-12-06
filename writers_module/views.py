from django.shortcuts import render
from django.views.generic import ListView, DetailView

from books_module.models import Books
from writers_module.models import Writers, Translators


class WritersListView(ListView):
    model = Writers
    template_name = 'writers_module/writers_list_page.html'
    context_object_name = 'writers'
    paginate_by = 6

    def get_queryset(self):
        query = super(WritersListView, self).get_queryset()
        query = query.filter(is_active=True, is_delete=False).all()
        return query


class WritersDetailView(DetailView):
    model = Writers
    template_name = 'writers_module/writers_detail_page.html'
    context_object_name = 'writer'

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        context = super(WritersDetailView, self).get_context_data()
        context['related_books'] = Books.objects.filter(book_writer__id=pk, is_active=True, is_delete=False).all()
        return context


class TranslatorsListView(ListView):
    model = Translators
    template_name = 'writers_module/translators_list_page.html'
    context_object_name = 'translators'
    paginate_by = 6

    def get_queryset(self):
        query = super(TranslatorsListView, self).get_queryset()
        query = query.filter(is_active=True, is_delete=False)
        return query


class TranslatorsDetailView(DetailView):
    model = Translators
    template_name = 'writers_module/translators_detail_page.html'
    context_object_name = 'translator'

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        context = super(TranslatorsDetailView, self).get_context_data()
        context['related_books'] = Books.objects.filter(book_translator__id=pk, is_active=True, is_delete=False).all()
        return context
