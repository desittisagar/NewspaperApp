from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Article
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
# Create your views here.

#ArticleDetailView, ArticleUpdateView, ArticleDeleteView

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