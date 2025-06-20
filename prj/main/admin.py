from django.contrib import admin
from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ["id","name","year"]




admin.site.register(Movie, MovieAdmin)
# Register your models here.