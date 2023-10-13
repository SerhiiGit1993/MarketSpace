from django.urls import path
from .views import *
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('published/', BoardListView.as_view()),
    path('published/<slug:url>/', BoardDetailView.as_view()),
    path('comments/', CommentsAddView.as_view()),


]

# urlpatterns += doc_urls