from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Article, Comment
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
# Create your views here.

#ArticleDetailView, ArticleUpdateView, ArticleDeleteView
class CommentCreateView(LoginRequiredMixin, CreateView):
	model = Comment
	template_name = 'comment_new.html'
	fields = ('comment',)
	login_url = 'login'
	success_url = reverse_lazy('article_list')

	def form_valid(self, form):
		form.instance.author = self.request.user
		pk = self.kwargs.get('pk')
		obj = Article.objects.filter(pk=pk)
		#print(obj.first())
		form.instance.article = obj.first()
		#print("try", self.request.POST)
		#pk = self.kwargs.get('pk')
		#print(Article.objects.filter(pk=pk))
		print(self.kwargs.get('pk'))
		print(form.instance.author)
		print(form.instance)
		#print(form.instance.article)
		#print(Comment.article.filter(pk=pk))
		# print("\n\n")
		#form.instance.article = self.request.article
		return super().form_valid(form)


class ArticleCreateView(LoginRequiredMixin, CreateView):
	model = Article
	template_name = 'article_new.html'
	fields = ('title', 'body')
	login_url = 'login'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class ArticleListView(LoginRequiredMixin, ListView):
	template_name = 'article_list.html'
	model = Article
	login_url = 'login'


class ArticleDetailView(LoginRequiredMixin, DetailView):
	template_name = 'article_detail.html'
	model = Article
	login_url = 'login'

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
	template_name = 'article_edit.html'
	model = Article
	fields = ('title', 'body')
	login_url = 'login'

	def dispatch(self, request, *args, **kwargs):
		obj = self.get_object()
		if obj.author != self.request.user:
			raise PermissionDenied
		return super().dispatch(request, *args, **kwargs)


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
	template_name = 'article_delete.html'
	model = Article
	success_url = reverse_lazy('article_list')
	login_url = 'login'

	def dispatch(self, request, *args, **kwargs):
		obj = self.get_object()
		if obj.author != self.request.user:
			raise PermissionDenied
		return super().dispatch(request, *args, **kwargs)