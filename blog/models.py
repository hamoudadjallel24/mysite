from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django. urls import reverse
from taggit.managers import TaggableManager



class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

class Post(models.Model):
    
    class Status(models.TextChoices):
        DRAFT = 'DF' , 'Draft'
        PUBLISHED = 'PB' , 'Published'

    tags = TaggableManager()
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    class Meta:
        ordering = ['-publish']
        indexes = [ models.Index(fields=[ '-publish' ]),]

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year,  self.publish.strftime('%m'),
                                            self.publish.strftime('%d'), self.slug])
   
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)
        def __str__(self):
            return 'Comment by {} on {}'.format(self.name, self.post)
