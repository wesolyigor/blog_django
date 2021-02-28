from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.articles_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.articles_detail, name='post_detail'),
]
