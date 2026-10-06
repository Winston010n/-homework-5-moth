from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Books
from .serializers import BooksSerializer


class BooksListApi(APIView):
    def get(self, request):
        books = Books.objects.all()
        serializer = BooksSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)