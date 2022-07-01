from django.shortcuts import render
from rest_framework.generics import ListAPIView 
from .models import *
from .serializers import LinkSerializer
# Create your views here.

class PostListApi(ListAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
    
class PostCreateApi(ListAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
    
class PostDetailApi(ListAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
    
class PostUpdateApi(ListAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
    
class PostDeleteApi(ListAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer