import telebot   
from config import keys, TOKEN
from extensions import ConversionException, Converter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start", "help"])
def welcome(message: telebot.types.Message):
    text = "Для начала работы введите команду в формате:\n <имя валюты> \
<в какую валюту перевести> \
<количество валюты> \nСписок валют: /values"
    bot.reply_to(message, text)
    
    
@bot.message_handler(commands=["values"])
def values(message: telebot.types.Message):
    text = "Валюты: "
    for key in keys.keys():
        text = "\n".join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=["text"])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(" ")
        
        if  len(values) != 3:
            raise ConversionException("Слишком много параметров.")
        
        base, to, amount = values
        result = Converter.get_price(base, to, amount)
    except ConversionException as e:
        bot.reply_to(message, f"Ошибка пользователя\n{e}")
    except Exception as e:
        bot.reply_to(message, f"Не удалось обработать команду\n{e}")
    else:     
        text = f"{amount} {base} в {to} - {result}"
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)