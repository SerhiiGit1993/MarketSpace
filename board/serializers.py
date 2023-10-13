from rest_framework import serializers
from .models import *


class BoardListSerializer(serializers.ModelSerializer):
    '''головна сторінка'''
    class Meta:
        model = Board
        fields = ('title', 'price', 'board_img', 'cat', 'create_date')


class CommentsAddSerializer(serializers.ModelSerializer):
    """додавання коментрів"""
    class Meta:
        model = Comments
        fields = '__all__'


class CommentsShowSerializer(serializers.ModelSerializer):
    """вивід коментарів"""
    class Meta:
        model = Comments
        fields = ('user', 'text')


class BoardDetailSerializer(serializers.ModelSerializer):
    """інформація про конкретний товар"""
    cat = serializers.SlugRelatedField(slug_field='cat_name', read_only=True)
    comments = CommentsShowSerializer(many=True)

    class Meta:
        model = Board
        exclude = ('is_published', 'url', 'id',)



