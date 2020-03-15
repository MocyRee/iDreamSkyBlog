from django.shortcuts import render
from .models import Article, Category, Tag, Nav, NavCollapse, Links, BlogSettings
from django.views.generic import ListView, DetailView
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404




def index(request):
    return render(request, 'blog/index.html')




class AboutView(ListView):
   template_name = 'blog/about.html' 
   context_object_name = 'about'
   queryset = Article.objects.get(title='about')

class ArticleListView(ListView):
    template_name = 'blog/list.html'
    context_object_name = 'articles'
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    template_name = 'blog/detail.html'
    context_object_name = 'article'
    model = Article
    