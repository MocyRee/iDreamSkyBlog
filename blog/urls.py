from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='detail'),
    path('article/article-list/', views.ArticleListView.as_view(), name='article_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('', views.index, name='index')
    # path('', views.IndexView.as_view(), name='index'),
]
