from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Article
from django.urls import reverse_lazy
# Create your views here.

#ArticleDetailView, ArticleUpdateView, ArticleDeleteView

class ArticleCreateView(CreateView):
	model = Article
	template_name = 'article_new.html'
	fields = ('title', 'body')

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class ArticleListView(ListView):
	template_name = 'article_list.html'
	model = Article

class ArticleDetailView(DetailView):
	template_name = 'article_detail.html'
	model = Article

class ArticleUpdateView(UpdateView):
	template_name = 'article_edit.html'
	model = Article
	fields = ('title', 'body')

class ArticleDeleteView(DeleteView):
	template_name = 'article_delete.html'
	model = Article
	success_url = reverse_lazy('article_list')