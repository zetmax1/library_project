from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet

from .serializers import BookSerializer
from .models import Book
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
# from django.shortcuts import get_object_or_404


# class BookListApiView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookListApiView(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            'Status': f'Returned {len(books)} books',
            'books': serializer_data
        }
        return Response(data)


# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDetailApiView(APIView):
    
    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            serializer_data = BookSerializer(book).data
            data = {
                'status': 'successfull',
                'books': serializer_data,
            }
            return Response(data)
        except Exception:
            return Response({
                'status': 'does not exist',
                'message': 'book was not found',
            }, status=status.HTTP_404_NOT_FOUND)

class BookDeleteApiView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookUpdateApiView(APIView):

    def put(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        data = request.data
        serializer_data = BookSerializer(instance=book, data=data, partial=True)
        if serializer_data.is_valid(raise_exception=True):
           book_saved = serializer_data.save()

        return Response({
                'status': 'successfull',
                'message': f'book was updated',
            })

# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookCreateApiView(APIView):

    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {
                'Status': 'Books are saved to database',
                'books': data,
            }
            return Response(data)
   
# class BookUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookUpdateDeleteView(APIView):

    def delete(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        book.delete()

        return Response({
            'status':True,
            'message': 'book successfully deleted'
        }, status=status.HTTP_200_OK)

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#api view with function
@api_view(['GET'])
def book_list_view(request, *args, **kwargs):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
