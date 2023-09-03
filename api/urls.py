from django.urls import path
from . import views

urlpatterns = [
  # path('articles/', views.article_list, name='articles'),
  # path('articles/<int:pk>', views.article_details, name='article-details'),
  path('articles/', views.ArticleList.as_view(), name='articles'),
  path('articles/<int:pk>', views.ArticleDetails.as_view(), name='article-details'),

]