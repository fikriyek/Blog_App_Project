from django.urls import path, include
from .views import CategoryListCV, CategoryCreateCV, CategoryUpdateCV, CategoryDeleteCV
from .views import CommentListCV, CommentCreateCV, CommentUpdateCV, CommentDeleteCV
from .views import BlogPageListCV

urlpatterns = [
    # Category Table
    path('categoryListCV/', CategoryListCV.as_view()),
    path('categoryCreateCV/', CategoryCreateCV.as_view()),
    path('categoryUpdateCV/<int:pk>/', CategoryUpdateCV.as_view()),
    path('categoryDeleteCV/<int:pk>/', CategoryDeleteCV.as_view()),

    # Comment
    path('commentListCV/', CommentListCV.as_view()),
    path('commentCreateCV/', CommentCreateCV.as_view()),
    path('commentUpdateCV/<int:pk>/', CommentUpdateCV.as_view()),
    path('commentDeleteCV/<int:pk>/', CommentDeleteCV.as_view()),

    # Blog
    path('blogListCV/', BlogPageListCV.as_view()),
]