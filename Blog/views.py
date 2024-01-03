from django.shortcuts import render, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import CategoryTable, Comment, Blog
from .serializers import CategorySerializer, BlogSerializer, UserBlogSerializer, CommentSerializer
from .permissions import IsStaffOrReadOnly, IsOwnerOrReadOnly

# Create your views here.
# Category Table concrete view for GET
class CategoryListCV(ListAPIView):
    queryset = CategoryTable.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

# Category Table concrete view for POST
class CategoryCreateCV(CreateAPIView):
    queryset = CategoryTable.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsStaffOrReadOnly]

# Category Table concrete view for PUT/PATCH
class CategoryUpdateCV(UpdateAPIView):
    queryset = CategoryTable.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsStaffOrReadOnly]

# Category Table concrete view for DELETE
class CategoryDeleteCV(DestroyAPIView):
    queryset = CategoryTable.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsStaffOrReadOnly]

# Comment concrete view for GET
class CommentListCV(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class =  CommentSerializer
    permission_classes = [AllowAny]

# Comment concrete view for POST
class CommentCreateCV(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

# Comment concrete view for PUT
class CommentUpdateCV(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

# Comment concrete view for DELETE
class CommentDeleteCV(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

# Blog concrete view for GET
class BlogPageListCV(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = UserBlogSerializer
    permission_classes = [AllowAny]
    
    def get_serializer_class(self):
        serializer = super().get_serializer_class()

        if self.request.user.is_staff:
            return BlogSerializer
        return serializer 

# Blog concrete view for POST
class BlogPageCreateCV(CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = UserBlogSerializer
    permission_classes = [IsOwnerOrReadOnly, IsStaffOrReadOnly] 

    def get_serializer_class(self):
        serializer = super().get_serializer_class()

        if self.request.user.is_staff:
            return BlogSerializer
        return serializer  

# Blog concrete view for PUT   
class BlogPageUpdateCV(UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = UserBlogSerializer
    permission_classes = [IsOwnerOrReadOnly, IsStaffOrReadOnly] 

    def get_serializer_class(self):
        serializer = super().get_serializer_class()

        if self.request.user.is_staff:
            return BlogSerializer
        return serializer  

# Blog concrete view for DELETE  
class BlogPageDeleteCV(DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = UserBlogSerializer
    permission_classes = [IsOwnerOrReadOnly, IsStaffOrReadOnly] 

    def get_serializer_class(self):
        serializer = super().get_serializer_class()

        if self.request.user.is_staff:
            return BlogSerializer
        return serializer  