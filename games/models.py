from django.db import models
import jsonfield  # pip install django-jsonfield
from slugify import slugify
from django.contrib.auth.models import User

class Game(models.Model):
    """
    Game model. Define game attributes.
    """
    high_scores_default = {"first": 0.0,
                           "second": 0.0,
                           "third": 0.0}

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=50, unique=True) 
    price = models.FloatField(default=0.0)
    url = models.URLField(blank=True)
    high_scores = jsonfield.JSONField(default=high_scores_default)
    description = models.TextField(default = "", blank=True)
    date = models.DateTimeField(auto_now_add = True)
    thumb = models.ImageField(default='default.png', blank=True)
    developer = models.ForeignKey(User, default=None, on_delete='CASCADE')

    def __str__(self):
        return self.title

    def snippet(self):
        return self.description[:50] + '...'