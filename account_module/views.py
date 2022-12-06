from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.http import HttpResponse, Http404, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views import View
from account_module.forms import RegisterForm, LoginForm, ForgetPassForm, ResetPassForm
from account_module.models import User, Subscriber
from utils.email_service import send_email


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()

        return render(request, 'account_module/register_page.html', context={
            'register_form': register_form
        })

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'ایمبل تکراری است')
            else:
                new_user = User(
                    email=user_email,
                    email_active_code=get_random_string(72),
                    username=user_email,
                    is_active=False
                )
                new_user.set_password(user_password)
                new_user.save()
                send_email('فعالسازی حساب کاربری', new_user.email, {'user': new_user}, 'emails/active_account.html')
                messages.success(request, 'کد فعالسازی برای شما ایمیل شد. حساب ایمیل خود را چک کنید.')
                return redirect(request.META.get('HTTP_REFERER', '/'))

        return render(request, 'account_module/register_page.html', context={
            'register_form': register_form
        })


class ActiveAccount(View):
    def get(self, request, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.save()
                return redirect(reverse('login_page'))
            else:
                return HttpResponse('حساب کاربری شما قبلاً فعال شده است')

        raise Http404


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        return render(request, 'account_module/login_page.html', {
            'login_form': login_form
        })

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_password = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'حساب کاربری شما فعال نمیباشد')
                else:
                    password_is_correct = user.check_password(user_password)
                    if password_is_correct:
                        login(request, user)
                        return redirect(reverse('user_panel_main_page'))
                    else:
                        login_form.add_error('password', 'حساب کاربری با این مشخصات یافت نشد')
            else:
                login_form.add_error('email', 'حساب کاربری با این مشخصات یافت نشد')

        return render(request, 'account_module/login_page.html', {
            'login_form': login_form
        })


class ForgetPassView(View):
    def get(self, request: HttpRequest):
        forget_pass_form = ForgetPassForm()
        return render(request, 'account_module/forget_pass_page.html', {
            'forget_pass_form': forget_pass_form
        })

    def post(self, request: HttpRequest):
        forget_pass_form = ForgetPassForm(request.POST)
        if forget_pass_form.is_valid():
            user_email = forget_pass_form.cleaned_data.get('email')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is None:
                return redirect(reverse('login_page'))
            send_email('بازیابی کلمه عبور', user.email, {'user': user}, 'emails/forgot_pass.html')
            return redirect(reverse('user_panel_main_page'))


class ResetPassView(View):
    def get(self, request: HttpRequest, activation_code):
        user: User = User.objects.filter(email_active_code__iexact=activation_code).first()
        if user is None:
            return redirect(reverse('login_page'))

        reset_pass_form = ResetPassForm()
        return render(request, 'account_module/reset_pass_page.html', {
            'reset_pass_form': reset_pass_form,
            'user': user
        })

    def post(self, request: HttpRequest, activation_code):
        reset_pass_form = ResetPassForm(request.POST)
        user: User = User.objects.filter(email_active_code__iexact=activation_code).first()
        if reset_pass_form.is_valid():
            if user is None:
                return redirect(reverse('login_page'))

            user_new_password = reset_pass_form.cleaned_data.get('password')
            user.set_password(user_new_password)
            user.email_active_code = get_random_string(72)
            user.is_active = True
            user.save()
            return redirect(reverse('login_page'))

        return render(request, 'account_module/reset_pass_page.html', {
            'reset_pass_form': reset_pass_form,
            'user': user
        })


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login_page'))


def subscribe_newsletter(request: HttpRequest):
    if request.POST:
        subscriber_email = request.POST.get('newsletter_subscribe')
        if not subscriber_email:
            messages.error(request, 'ایمیل خود را وارد کنید')
            return redirect('/')
        if Subscriber.objects.filter(email__iexact=subscriber_email).first():
            messages.error(request, 'این ایمیل قبلا ثبت شده است.')
            return redirect('/')

        try:
            validate_email(subscriber_email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect('/')

        new_subscriber = Subscriber()
        new_subscriber.email = subscriber_email
        new_subscriber.save()
        messages.success(request, 'ایمیل شما با موفقیت ثبت شد.')
    return redirect(request.META.get('HTTP_REFERER', '/'))
