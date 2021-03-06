from django.urls import path, include
#from django.views.generic.base import TemplateView
from .views import (ArticleListView, 
	ArticleDetailView, 
	ArticleUpdateView, 
	ArticleDeleteView, 
	ArticleCreateView,
	CommentCreateView,
	)


urlpatterns = [
    path('',ArticleListView.as_view(), name = 'article_list'),
    path('new/',ArticleCreateView.as_view(), name = 'article_new'),
    path('<int:pk>/comment/',CommentCreateView.as_view(), name = 'comment_new'),
    path('<int:pk>/',ArticleDetailView.as_view(), name = 'article_detail'),
    path('<int:pk>/edit/',ArticleUpdateView.as_view(), name = 'article_edit'),
    path('<int:pk>/delete/',ArticleDeleteView.as_view(), name = 'article_delete'),
]