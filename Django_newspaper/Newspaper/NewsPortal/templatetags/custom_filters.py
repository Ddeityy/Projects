from django import template

register = template.Library()

CURRENCIES_SYMBOLS = {
   'rub': '₽',
   'usd': '$',
}

@register.filter()
def currency(value, code='rub'):
   postfix = CURRENCIES_SYMBOLS[code]
   return f'{value} {postfix}'

@register.filter()
def censor(value):
   for i in curselist:
      if i.find(value):
         value = value.replace(i[1::], "*" * len(i))
      else:
         return f'{value}'
   return f'{value}'

curselist =[
   'блядки',
   'блядовать',
   'блядство',
   'блядь',
   'блять',
   'бугор',
   'в пизду',
   'встать раком',
   'выёбываться',
   'гандон',
   'говно',
   'говнюк',
   'дать пизды',
   'дерьмо',
   'дрочить',
   'ёбарь',
   'ебать',
   'ебать',
   'ебло',
   'ебнуть',
   'ёб твою мать',
   'жопа',
   'жополиз',
   'манда',
   'мандавошка',
   'мудак',
   'мудила',
   'мудозвон',
   'наебать',
   'наебениться',
   'наебнуться',
   'нахуй',
   'нахуя',
   'нахуячиться',
   'нихуя',
   'охуеть',
   'охуительно',
   'сиськи',
   'спиздить',
   'срать',
   'ссать',
   'траxать',
   'хуёво',
   'хуёвый',
   'хуеплет',
   'хуйло',
   'хуйней страдать',
   'хуйня',
   'хуй',
   'хуйнуть',
   'хуй пинать'
]