from rest_framework import serializers

from .models import CategoryTable, Comment, PostViews, Likes, Blog

# Category Table serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryTable
        fields = (
            'name'
        )

# Comment serializer
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    blog = serializers.StringRelatedField()
    blog_id = serializers.IntegerField()

    class Meta:
        model = Comment
        fields = (
            'user',
            'blog_id',
            'blog',
            'content',
            'time_stamp',            
        )
        read_only_fields = ('user', 'blog_id', )

    # Getting id automatically from token information django
    def create(self, validated_data):
         validated_data['user_id'] = self.context['request'].user.id
         comment = Comment.objects.create(**validated_data)
         return comment

# Post Views serializer
class PostViewsSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    blog = serializers.StringRelatedField()
    blog_id = serializers.IntegerField()

    class Meta:
        model = PostViews
        fields = (
            'user',
            'blog_id',
            'blog',
            'post_views',
            'time_stamp',
        )
        read_only_fields = ('user', 'blog_id', )

    # Getting id automatically from token information django
    def create(self, validated_data):
         validated_data['user_id'] = self.context['request'].user.id
         post_view = PostViews.objects.create(**validated_data)
         return post_view

# Likes serializer
class LikesSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    blog = serializers.StringRelatedField()
    blog_id = serializers.IntegerField()

    class Meta:
        model = Likes
        fields = (
            'user',
            'blog_id',
            'blog',
            'likes',
        )
        read_only_fields = ('user', 'blog_id', )
    
    # Getting id automatically from token information django
    def create(self, validated_data):
        validated_data['user_id'] = self.context['request'].user.id
        like = Likes.objects.create(**validated_data)
        return like

# Blog serializer    
class BlogSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    category_id = serializers.IntegerField()

    count_of_comments = serializers.SerializerMethodField()
    count_of_views = serializers.SerializerMethodField()
    count_of_likes = serializers.SerializerMethodField()

    comment = CommentSerializer(many=True, read_only=True)
    post_view = PostViewsSerializer(many=True, read_only=True)
    like = LikesSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = (
            'user',
            'title', 
            'content',
            'category_id',
            'category',
            'comment',
            'count_of_comments',
            'post_view',
            'count_of_views',
            'like',
            'count_of_likes',
            'status',
            'published_date',
            )
        read_only_fields = ('user',)

    def get_count_of_comments(self, obj):
        return obj.comment.count()
    
    def get_count_of_views(self, obj):
        return obj.post_views.filter(post_views=True).count()
        # return obj.view.count()
    
    def get_count_of_likes(self, obj):
        return obj.likes.filter(likes=True).count()
    
    # Getting id automatically from token information django
    def create(self, validated_data):
        validated_data['user_id'] = self.context['request'].user.id
        instance = Blog.objects.create(**validated_data)
        return instance
    
# User Blog serializer
class UserBlogSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    category_id = serializers.IntegerField()

    count_of_comments = serializers.SerializerMethodField()
    count_of_views = serializers.SerializerMethodField()
    count_of_likes = serializers.SerializerMethodField()

    comment = CommentSerializer(many=True, read_only=True)
    post_view = PostViewsSerializer(many=True, read_only=True)
    like = LikesSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = (
            'user',
            'title', 
            'content',
            'category_id',
            'category',
            'comment',
            'count_of_comments',
            'post_view',
            'count_of_views',
            'like',
            'count_of_likes',
            'published_date',
            )
        read_only_fields = ('user',)

    def get_count_of_comments(self, obj):
        return obj.comment.count()
    
    def get_count_of_views(self, obj):
        return obj.post_views.filter(post_views=True).count()
        # return PostViews.objects.count()
    
    def get_count_of_likes(self, obj):
        return obj.likes.filter(likes=True).count()
    
    # Getting id automatically from token information django
    def create(self, validated_data):
        validated_data['user_id'] = self.context['request'].user.id
        instance = Blog.objects.create(**validated_data)
        return instance