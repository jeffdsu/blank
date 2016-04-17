from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.decorators import detail_route

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer