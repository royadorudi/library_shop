from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import FormView
from account_module.models import User
from blog_module.models import BlogList
from books_module.models import Books
from contact_module.forms import ContactUsModelForm
from contact_module.models import ContactUs
from siteSetting_module.models import AboutUs


class HomeView(FormView):
    template_name = 'home_module/home_page.html'
    form_class = ContactUsModelForm
    success_url = '/contact-us/response/'

    def form_valid(self, form):
        form.save()
        return super(HomeView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()
        context['info'] = AboutUs.objects.first()
        context['blogs_list'] = BlogList.objects.filter(is_active=True).order_by('-date')[:2]
        context['all_books'] = Books.objects.filter(is_active=True, is_delete=False, category__is_active=True,
                                                    category__is_delete=False).all()[:3]
        context['contact'] = ContactUs.objects.filter(is_read_by_admin=True).all().order_by('-date')[:3]
        context['newest_books'] = Books.objects.filter(is_active=True, is_delete=False, category__is_active=True,
                                                       category__is_delete=False).order_by('-submit_date').all()[:3]
        return context


def header_component(request: HttpRequest):
    return render(request, 'shared/header_component.html')


def footer_component(request: HttpRequest):
    about_us_info = AboutUs.objects.first()
    return render(request, 'shared/footer_component.html', {
        'info': about_us_info
    })


def about_us(request: HttpRequest):
    info = AboutUs.objects.first()
    context = {
        'info': info
    }
    return render(request, 'home_module/about_page.html', context)
