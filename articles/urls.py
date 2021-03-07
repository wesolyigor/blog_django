from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.articles_list, name='articles_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:article>/', views.articles_detail, name='articles_detail'),
    path('tag/<slug:tag_slug>/', views.articles_list, name='article_list_by_tag'),
    path('<str:category>', views.categories_list, name='categories_list'),
]
