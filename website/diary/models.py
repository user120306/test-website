
from __future__ import unicode_literals

from django.utils import timezone

from django.contrib.auth.models import Permission, User

from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    desc = models.TextField()
    cover_photo = models.FileField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    tag = models.TextField(null=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('diary:index')

    def ordered_entry_set(self):
        return self.entry_set.all().order_by('entry_date')

class Entry(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    short_text = models.CharField(max_length=200)
    long_text = models.TextField()
    order = models.IntegerField(default=0,max_length=10)
    map_url = models.CharField(max_length=4000,null=True, blank=True)
    photo_url = models.FileField(null=True, blank=True)
    book_url = models.CharField(max_length=3000,null=True, blank=True)
    song_url = models.CharField(max_length=3000,null=True, blank=True)
    site_url = models.CharField(max_length=3000,null=True, blank=True)
    entry_date = models.DateTimeField(
            default=timezone.now)

    class Meta:
       ordering = ['-entry_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('diary:post-detail', kwargs={'pk':self.post.pk})
        #return reverse('diary:index')