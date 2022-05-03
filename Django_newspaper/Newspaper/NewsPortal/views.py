from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime



class NewsList(ListView):
    model = Post
    ordering = '-creation_timedate'
    template_name = 'news.html'
    context_object_name = 'news'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context
    
class PostDetail(DetailView):
    model = Post
    template_name = 'article.html'
    context_object_name = 'article'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
   

