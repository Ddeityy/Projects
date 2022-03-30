import telebot   
from config import TOKEN
from extensions import ConversionException, Converter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start", "help"])
def welcome(message: telebot.types.Message):
    text = "Enter:\n <base currency> \
<output currency> \
<amount>"
    bot.reply_to(message, text)
    
    
@bot.message_handler(content_types=["text"])
def convert_(message: telebot.types.Message):
    try:
        values = message.text.split(" ")
        
        if len(values) > 3:
            raise ConversionException("Too many variables.")
        elif len(values) < 3:
            raise ConversionException("Not enough variables")
        
        base, to, amount = values
        
        result = Converter.convert(base, to, amount)
    except ConversionException as e:
        bot.reply_to(message, f"User error\n{e}")
    except Exception as e:
        bot.reply_to(message, f"Wrong command\n{e}")
    else:     
        text = f"{amount} {base} in {to} is {result}"
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)