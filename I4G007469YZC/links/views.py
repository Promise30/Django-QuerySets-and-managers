from django.shortcuts import render
from .models import Link
from rest_framework import viewsets
from .serizliers import LinkSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
# Create your views here.
class PostListApi(ListAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostCreateApi(CreateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostDetailApi(RetrieveAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostUpdateApi(UpdateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostDeleteApi(DestroyAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer