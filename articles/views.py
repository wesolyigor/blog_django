from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

# Create your views here.
from articles.models import Article


def articles_list(request):
    articles = Article.published.all()
    paginator = Paginator(articles, 3)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render(request, 'articles/list_articles.html', {'page': page, 'articles': articles})


def articles_detail(request, year, month, day, article):
    article = get_object_or_404(Article, slug=article,
                                status='published',
                                publish__year=year,
                                publish__month=month,
                                publish__day=day)
    return render(request, 'articles/article_details.html', {'article': article})
