from django.shortcuts import render
from .models import Article, Category, Tag, Nav, NavCollapse, Links, BlogSettings, Log
from django.views.generic import ListView, DetailView
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
import markdown



def index(request):
    return render(request, 'blog/index.html')

#Article View

class ArticleListView(ListView):
    template_name = 'blog/list.html'
    context_object_name = 'articles'

class ArticleListView(ArticleListView):
    queryset = Article.objects.all()

class ArticleByTagView(ArticleListView):
    def get_queryset(self):
        tag_name = self.kwargs['tag_name']
        tag = get_object_or_404(Tag, slug=tag_name)
        articles = Article.objects.filter(tags=tag)
        return articles

class ArticleByCategoryView(ArticleListView):
    def get_queryset(self):
        category_name = self.kwargs['category_name']
        category = get_object_or_404(Category, slug=category_name)
        articles = Article.objects.filter(category=category)
        return articles


    
class IndexView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    queryset = Article.objects.all().order_by('-order')[:6]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latestlog'] = Log.objects.all()[0]
        context['logs'] = Log.objects.all()[1:3]
        context['categories'] = Category.objects.filter(display=True)
        return context

class AboutView(ListView):
    template_name = 'blog/about.html' 
    context_object_name = 'about'
    queryset = Article.objects.get(title='about')

    def get_queryset(self):
        post = super().get_queryset()
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])
        post.body = md.convert(post.body)
        return post

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
