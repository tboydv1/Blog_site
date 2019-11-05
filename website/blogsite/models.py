from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(default=timezone.now() , null = True)
    status = models.IntegerField(choices=STATUS, default=0)

    def publish(self):
        self.published_date = timezone.now();
        self.save();

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title