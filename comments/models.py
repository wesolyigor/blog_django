from django.db import models

from articles.models import Article


class Comment(models.Model):
    article = models.ForeignKey(Article,
                                on_delete=models.CASCADE,
                                related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Komentarz dodany przez {} dla artykułu "{}"'.format(self.name, self.article)
