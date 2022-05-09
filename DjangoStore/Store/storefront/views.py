from django.views.generic import *
from django.urls import *
from django.http import HttpResponsePermanentRedirect
from .models import Product
from .forms import ProductForm
from .filters import ProductFilter

class ProductsList(ListView):
    model = Product
    ordering = 'name'
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 2

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # self.request.GET содержит объект QueryDict
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = ProductFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context
    
class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next_sale'] = None
        return context
   

class ProductCreate(CreateView):
    form_class = ProductForm
    model = Product
    template_name = 'product_edit.html'
    
class ProductUpdate(UpdateView):
    form_class = ProductForm
    model = Product
    template_name = 'product_edit.html'
    
class ProductDelete(DeleteView):
    form_class = ProductForm
    model = Product
    success_url = reverse_lazy('product_list')