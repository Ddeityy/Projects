from django import template


register = template.Library()


# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.

CURRENCIES_SYMBOLS = {
   'rub': '₽',
   'usd': '$',
}

@register.filter()
def currency(value, code='rub'):
   postfix = CURRENCIES_SYMBOLS[code]
   return f'{value}{postfix}'