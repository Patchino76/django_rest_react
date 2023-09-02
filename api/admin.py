from django.contrib import admin
from .models import Article

# Register your models here.
# first method
# admin.site.register(Article) 

#second custom registration method
@admin.register(Article)
class ArticleModel(admin.ModelAdmin):
  list_filter = ('title', 'description')
  list_display = ('title', 'description')