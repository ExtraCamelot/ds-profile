import telebot
from config import keys, TOKEN
from extensions import ConvertionException, CurrencyConverter

bot = telebot.TeleBot(TOKEN) # объект бота, в аргумент передаём токен от созданного бота в BotFather


# обработчик комманд start и help
@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Здравствуйте! Этот бот умеет быстро конвертировать валюту из одной в другую на основе актуального курса.' \
           '\nЧтобы начать работу введите команду боту в следующем формате: ' \
           '\n<название валюты> <в какую валюту перевести> <количество переводимой валюты>' \
           '\nНапример, доллар рубль 1' \
           '\nИ нажмите кнопку отправки сообщения.' \
           '\nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)

# обработчик комманды values - список доступных валют для конвертации
@bot.message_handler(commands=['values'])
def help(message: telebot.types.Message):
    text = 'Доступные валюты: '
    for key in keys.keys():
         text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

# обработчик-конвертатор
@bot.message_handler(content_types=['text', ])
def get_price(message: telebot.types.Message):
    try:
        values = message.text.split(' ')  # значения, которые ввёл пользователь
        if len(values) != 3:  # если пользователь ввёл больше 3 парметров, вывести ошибку
            raise ConvertionException('Неверно указаны параметры! Введите в формате: <валюта 1> <валюта 2> <кол-во>')
        base, quote, amount = values  # приравнивание переменых значениям из списка
        base = base.lower()    # введённый аргумент не чувствителен к регистру
        quote = quote.lower()    # введённый аргумент не чувствителен к регистру
        total_base = CurrencyConverter.get_price(base, quote, amount)
        total_base = float(total_base) * float(amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {base} в {quote} = {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True) # запуск бота

