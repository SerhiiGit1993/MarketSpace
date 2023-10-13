from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions


from .models import *
from .serializers import *


class BoardListView(APIView):
    """головна сторінка"""
    def get(self, request):
        board = Board.objects.filter(is_published=True)
        serializer = BoardListSerializer(board, many=True)
        return Response(serializer.data)


class BoardDetailView(APIView):
    """детальна інформація про товар"""
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, url):
        board = Board.objects.get(url=url, is_published=True)
        serializer = BoardDetailSerializer(board)
        return Response(serializer.data)


class CommentsAddView(APIView):
    """додавання коментарів"""
    def post(self, request):
        comments = CommentsAddSerializer(data=request.data)
        if comments.is_valid():
            comments.save()
        return Response(status=201)






