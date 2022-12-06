from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import FormView
from contact_module.forms import ContactUsModelForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, 'dispatch')
class ContactUsView(FormView):
    template_name = 'contact_module/contact_page.html'
    form_class = ContactUsModelForm
    success_url = '/contact-us/response/'

    def form_valid(self, form):
        form.save()
        return super(ContactUsView, self).form_valid(form)


def response_page(request: HttpRequest):
    return render(request, 'contact_module/response_page.html')


