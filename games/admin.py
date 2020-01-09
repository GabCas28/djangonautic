from django.contrib import admin
from .models import Game

class GameAdmin(admin.ModelAdmin):
      prepopulated_fields = {"slug": ("title",)}
admin.site.register(Game, GameAdmin)
