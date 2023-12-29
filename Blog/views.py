# from django.shortcuts import render

# from rest_framework.generics import ListAPIView
# from rest_framework.permissions import IsAuthenticated, AllowAny

# from .models import CategoryTable, Blog
# from .serializers import CategorySerializer
# from .permissions import IsStaffOrReadOnly

# Create your views here.
# Category Table concrete view for GET
# class CategoryTableListCV(ListAPIView):
#     queryset = CategoryTable.objects.all()
#     serializer_class = CategorySerializer

# Category Table concrete view for POST
# class CategoryTableCreateCV(CreateAPIView):
#     queryset = CategoryTable.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = [IsStaffOrReadOnly]

# Category Table concrete view for PUT/PATCH
# class CategoryTableUpdateCV(UpdateAPIView):
#     queryset = CategoryTable.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = [IsStaffOrReadOnly]

# Category Table concrete view for DELETE
# class CategoryTableDeleteCV(DestroyAPIView):
#     queryset = CategoryTable.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = [IsStaffOrReadOnly]

# Blog concrete view for GET
# class BlogPageListCV(ListAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = UserBlogSerializer
#     permission_classes = [AllowAny]