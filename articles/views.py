from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.db.models import Count

# Create your views here.
from taggit.models import Tag

from articles.models import Article


def articles_list(request, tag_slug=None):
    articles = Article.published.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        articles = articles.filter(tags__in=[tag])

    paginator = Paginator(articles, 3)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render(request, 'articles/list_articles.html', {'page': page, 'articles': articles, 'tag': tag})


def articles_detail(request, year, month, day, article):
    article = get_object_or_404(Article, slug=article,
                                status='published',
                                publish__year=year,
                                publish__month=month,
                                publish__day=day,
                                )
    article_tags_id = Article.tags.values_list('id', flat=True)
    similar_articles = Article.published.filter(tags__in=article_tags_id).exclude(id=article.id)
    similar_articles = similar_articles.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:3]

    return render(request, 'articles/article_details.html', {'article': article, 'similar_articles': similar_articles})


def categories_list(request, category):
    articles_by_category = Article.published.filter(category=category)
    return render(request, 'articles/categories_list.html',
                  {'articles_by_category': articles_by_category, 'category': category})
