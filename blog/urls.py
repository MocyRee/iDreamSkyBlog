from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='detail'),
    path('article/article-list/', views.ArticleListView.as_view(), name='article_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('', views.IndexView.as_view(), name='index'),
    path('tag/<slug:tag_name>/', views.ArticleByTagView.as_view(), name='tag'),
    path('category/<slug:category_name>/', views.ArticleByCategoryView.as_view(), name='category')
    # path('', views.IndexView.as_view(), name='index'),
]
