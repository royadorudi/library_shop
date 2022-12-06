from django.urls import path
from user_pannel_module import views

urlpatterns = [
    path('', views.user_panel, name='user_panel_main_page'),
    path('edit-profile/', views.EditUserProfile.as_view(), name='edit_profile_page'),
    path('change-password/', views.ChangePassword.as_view(), name='change_password_page'),
    path('book-marks/', views.book_marks, name='book_marks_page'),
]
