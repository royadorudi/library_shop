from django.views.generic import ListView, DetailView
from blog_module.models import BlogList


class BlogListView(ListView):
    model = BlogList
    template_name = 'blog_module/blog_list_page.html'
    context_object_name = 'blog_list'
    paginate_by = 4

    def get_queryset(self):
        query = super(BlogListView, self).get_queryset()
        query = query.filter(is_active=True).order_by('-date')
        return query


class BlogDetailView(DetailView):
    model = BlogList
    template_name = 'blog_module/blog_detail_page.html'
    context_object_name = 'blog'


