from django.shortcuts import render, get_object_or_404

# Create your views here.
from articles.models import Article


def articles_list(request):
    articles = Article.published.all()
    return render(request, 'articles/list_articles.html', {'articles': articles})


def articles_detail(request, year, month, day, articles):
    articles = get_object_or_404(Article, slug=articles,
                                 status='published',
                                 publish__year=year,
                                 publish__month=month,
                                 publish__day=day)
    return render(request, 'blog/post/detail.html', {'articles': articles})

