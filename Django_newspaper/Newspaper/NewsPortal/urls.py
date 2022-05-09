from django.urls import path
from .views import *

urlpatterns = [
    path('', NewsList.as_view(), name='news_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('create/', NewsCreate.as_view(), name='news_create'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('articles/create/', ArticleCreate.as_view(), name='article_create'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('search/', SearchView.as_view(), name='search')
]
