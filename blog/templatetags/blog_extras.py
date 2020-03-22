from django import template
from ..models import Article, Category, Tag, BlogSettings, Nav, Log, Links


register = template.Library()



@register.inclusion_tag('blog/inclusions/recent_posts.html', takes_context=True)
def show_recent_articles(context, num=4):  
    return {
        'articles':Article.objects.all().order_by('-created_time')[:num],
    }


@register.inclusion_tag('blog/inclusions/footer.html', takes_context=True)
def footer(context):
    return {
        'tags':Tag.objects.all(),
        'links':Links.objects.filter(is_enable=True),
    }


@register.inclusion_tag('blog/inclusions/navbar.html', takes_context=True)
def navbar(context):
    return {
        "navbars": Nav.objects.all(),        
    }


@register.inclusion_tag('blog/inclusions/log.html', takes_context=True)
def log(context):
    return {
        'latest':Log.objects.all()[0],
        'logs':Log.objects.all()[1:3]
    }


@register.inclusion_tag('blog/inclusions/article.html', takes_context=True)
def article(context):
    return {
        'articles':Article.objects.all().order_by('-order')[:6],
    }
