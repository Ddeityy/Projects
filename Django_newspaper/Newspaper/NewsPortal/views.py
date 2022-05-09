from django.views.generic import *
from .models import *
from django.urls import *
from .filters import *
from django.views.generic import *
from .forms import *
from datetime import datetime



class NewsList(ListView):
    model = Post
    ordering = '-creation_timedate'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10
    
    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # self.request.GET содержит объект QueryDict
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filterset'] = self.filterset
        return context
    
class SearchView(ListView):
    template_name = 'search.html'
    model = Post
    ordering = '-creation_timedate'
    paginate_by = 10

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context
    
class PostDetail(DetailView):
    model = Post
    template_name = 'article.html'
    context_object_name = 'article'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
   
class NewsCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    success_url = reverse_lazy('news_list')
    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'N'
        return super().form_valid(form)
    

class ArticleCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    success_url = reverse_lazy('news_list')
    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'A'
        return super().form_valid(form)
    
    
class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    success_url = reverse_lazy('news_list')

    
class PostDelete(DeleteView):
    form_class = PostForm
    model = Post
    success_url = reverse_lazy('news_list')