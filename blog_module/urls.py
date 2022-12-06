from django.urls import path
from blog_module import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog_list_page'),
    path('<pk>/<str>/', views.BlogDetailView.as_view(), name='blog_detail_page'),
]
