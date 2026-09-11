from django.contrib import admin
from .models import Movie, Review
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    ordering = ('name',)
    search_fields = ('name',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'user', 'date', 'is_reported')
    list_filter = ('is_reported', 'date')
    search_fields = ('comment', 'user__username', 'movie_name')

admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin)