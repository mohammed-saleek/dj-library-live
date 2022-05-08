from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.homepage,name = 'homepage'),
    path('create-book/',views.book_register, name = 'books'),
    path('update-book/<int:pk>/',views.book_update, name = 'book_update'),
    path('delete/<str:pk>/',views.book_delete, name = 'book_delete'),
    path('details/<str:pk>/',views.book_details, name = 'book_details'),
    path('book_download/<str:pk>/',views.book_download, name='book_download'),
    path('contact-us/',views.contact_us, name='contact_us'),
]