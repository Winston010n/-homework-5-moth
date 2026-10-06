from django.urls import path

from .views import BooksListApi

urlpatterns = [
	path('books/', BooksListApi.as_view(), name='books-list'),
]