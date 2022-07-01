from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from .utils import generate_random_id

User = get_user_model()

# Create your models here.
class Link(models.Model):
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(max_length=200, blank=True, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
       self.identifier = slugify(generate_random_id())
       super(Link, self).save(*args, **kwargs)
       
    def __str__(self):
        return self.description
    
