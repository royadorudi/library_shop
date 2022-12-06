from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from account_module.models import User
from books_module.models import Books
from user_pannel_module.forms import EditProfileModelForm, ChangePasswordForm
from django.core.paginator import Paginator


@login_required
def user_panel(request: HttpRequest):
    return render(request, 'user_pannel_module/user_pannel_main_page.html')


@method_decorator(login_required, 'dispatch')
class EditUserProfile(View):
    def get(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_profile_form = EditProfileModelForm(instance=current_user)
        return render(request, 'user_pannel_module/edit_profile_page.html', {
            'user': current_user,
            'edit_profile_form': edit_profile_form
        })

    def post(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_profile_form = EditProfileModelForm(request.POST, request.FILES, instance=current_user)
        if edit_profile_form.is_valid():
            edit_profile_form.save(commit=True)
            messages.success(request, 'اطلاعاتت ویرایش شد!😎')

        return render(request, 'user_pannel_module/edit_profile_page.html', {
            'user': current_user,
            'edit_profile_form': edit_profile_form
        })


@method_decorator(login_required, 'dispatch')
class ChangePassword(View):
    def get(self, request: HttpRequest):
        change_pass_form = ChangePasswordForm()
        return render(request, 'user_pannel_module/change_pass_page.html', {
            'change_pass_form': change_pass_form
        })

    def post(self, request: HttpRequest):
        change_pass_form = ChangePasswordForm(request.POST)
        if change_pass_form.is_valid():
            user: User = User.objects.filter(id=request.user.id).first()
            if user.check_password(change_pass_form.cleaned_data.get('current_pass')):
                user.set_password(change_pass_form.cleaned_data.get('new_pass'))
                user.save()
                logout(request)
                return redirect(reverse('login_page'))
            else:
                change_pass_form.add_error('current_pass', 'کلمه عبور وارد شده صحیح نیست!')

        return render(request, 'user_pannel_module/change_pass_page.html', {
            'change_pass_form': change_pass_form
        })


@login_required
def book_marks(request: HttpRequest):
    user_id = request.user.id
    bookmarks = Books.objects.filter(bookmarks__id=user_id, is_active=True, is_delete=False, category__is_delete=False,
                                     category__is_active=True)
    page = request.GET.get('page')
    paginator = Paginator(list(bookmarks), per_page=5)
    page_obj = paginator.get_page(page)
    context = {
        'bookmarks': bookmarks,
        'page_obj': page_obj
    }
    return render(request, 'user_pannel_module/user_bookmarks.html', context)

