from django.urls import path

from home_module import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home_page'),
    path('about-us/', views.about_us, name='about_us_page'),
]
