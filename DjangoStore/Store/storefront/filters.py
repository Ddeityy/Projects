from django_filters import *
from .models import *


# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class ProductFilter(FilterSet):
    material = ModelMultipleChoiceFilter(
            field_name='productmaterial__material',
            queryset=Material.objects.all(),
            label="Materials",
            conjoined=True,
        )
        
    class Meta:
        # В Meta классе мы должны указать Django модель,
        # в которой будем фильтровать записи.
        model = Product
        # В fields мы описываем по каким полям модели
        # будет производиться фильтрация.
        fields = {
            'name': ['icontains'],
            'quantity': ['gt'],
            'price': ['lt', 'gt',]
        }