from django.urls import path

from account_module import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register_page'),
    path('login/', views.LoginView.as_view(), name='login_page'),
    path('logout/', views.LogoutView.as_view(), name='logout_page'),
    path('forget-pass/', views.ForgetPassView.as_view(), name='forget_pass_page'),
    path('reset-pass/<activation_code>', views.ResetPassView.as_view(), name='reset_pass_page'),
    path('active-account/<email_active_code>', views.ActiveAccount.as_view(), name='active_account_page'),
    path('subscribe-newsletter', views.subscribe_newsletter, name='subscribe_newsletter'),
]