from django.urls import path
from siteSetting_module import views

urlpatterns = [
    path('', views.search_box, name='search_box'),
]
