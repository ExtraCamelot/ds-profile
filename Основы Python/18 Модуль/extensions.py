import requests
import json
from config import keys

# отлов исключений
class ConvertionException(Exception):
    pass

class CurrencyConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        if quote == base:  # если валюта 1 равна валюте 2, то вывести ошибку
            raise ConvertionException('Указали одинаковые валюты! Введите в формате: <валюта 1> <валюта 2> <кол-во>')
        # проверка на наличие ошибок в ведённых пользователем аргументах
        try:
            quote_ticker = keys[base]
        except KeyError:
            raise ConvertionException(
                f'Не удалось обработать валюту "{base}"! Для просмотра списка доступных валют воспользуйтесь командой /values')
        try:
            base_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(
                f'Не удалось обработать валюту "{quote}"! Для просмотра списка доступных валют воспользуйтесь командой /values')
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(
                f'Не удалось обработать количество {amount}! Используйте цифры для ввода количства валюты для конвертации.')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[quote]]
        return total_base