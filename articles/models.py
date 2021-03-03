from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Article(models.Model):
    STATUS_CHOICE = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    CATEGORY_CHOICE = (
        ('sport', 'Sport'),
        ('electronics', 'Electronics'),
        ('politics', 'Politics'),
        ('literature', 'Literature'),
        ('news', 'News')
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_articles')
    image = models.ImageField(null=True, blank=True, upload_to='uploads/')
    lead = models.TextField(max_length=500)
    category = models.CharField(choices=CATEGORY_CHOICE, default='news', max_length=20)
    body = RichTextField(blank=True, null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='draft')

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articles:articles_detail',
                       args=[self.publish.year,
                             self.publish.strftime('%m'),
                             self.publish.strftime('%d'),
                             self.slug])


class Test(models.Model):
    body = RichTextField(blank=True, null=True)
