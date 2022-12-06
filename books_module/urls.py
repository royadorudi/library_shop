from django.urls import path
from . import views


urlpatterns = [
    path('', views.BooksListView.as_view(), name='book_list_page'),
    path('categories/', views.BookCategoriesView.as_view(), name='book_categories_page'),
    path('<pk>/<str>', views.BookCategoriesDetailView.as_view(), name='book_categories_detail_page'),
    path('book-detail/<pk>/<str>/', views.BookDetailView.as_view(), name='book_detail_page'),
    path('add-to-bookmarks/<pk>/', views.add_to_bookmark, name='add_to_bookmarks_page'),
    path('remove-from-bookmarks/<pk>/', views.remove_from_bookmark, name='remove_from_bookmarks_page'),
    path('download-file/<str:filename>/', views.download_file, name='download_file_page'),
    path('book-comments/<int:book_id>/<str:book_name>/<int:parent_id>/', views.comments_list_and_form,
         name='book_comments_page'),
    path('book-comments/<int:comment_id>/', views.delete_comment, name='delete_comment'),

]
