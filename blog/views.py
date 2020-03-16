from django.shortcuts import render
from .models import Article, Category, Tag, Nav, NavCollapse, Links, BlogSettings
from django.views.generic import ListView, DetailView
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
import markdown



def index(request):
    return render(request, 'blog/index.html')




class AboutView(ListView):
    template_name = 'blog/about.html' 
    context_object_name = 'about'
    queryset = Article.objects.get(title='about')

    def get_queryset(self):
        post = super().get_queryset()
        print(post)
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])
        post.body = md.convert(post.body)
        return post

class ArticleListView(ListView):
    template_name = 'blog/list.html'
    context_object_name = 'articles'
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    template_name = 'blog/detail.html'
    context_object_name = 'article'
    model = Article
    
    def get_object(self):
        post = super().get_object(queryset=None)
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])
        post.body = md.convert(post.body)
        return post