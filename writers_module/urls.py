from django.urls import path
from writers_module import views

urlpatterns = [
    path('writers-list/', views.WritersListView.as_view(), name='writers_list_page'),
    path('writer-detail/<pk>/<str>/', views.WritersDetailView.as_view(), name='writers_detail_page'),
    path('translators-list/', views.TranslatorsListView.as_view(), name='translators_list_page'),
    path('translators-detail/<pk>/<str>', views.TranslatorsDetailView.as_view(), name='translators_detail_page'),
]
