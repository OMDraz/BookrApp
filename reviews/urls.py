from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail_view, name='book_detail_view')
]