from django.shortcuts import render, get_object_or_404

from .models import Article
from .forms import CommentForm


def comment_detail(request):
    article = get_object_or_404(Article, status='published')
    comments = article.comments.filter(active=True)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,
                  '_comments.html',
                  {'comments': comments,
                   'comment_form': comment_form})


