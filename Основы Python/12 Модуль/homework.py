per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
user_money = int(input('Введите сумму (только цифры) для рассчёта годовой прибыли от депозита: '))
profit_tkb = int(user_money / 100 * per_cent['ТКБ'])
profit_skb = int(user_money / 100 * per_cent['СКБ'])
profit_vtb = int(user_money / 100 * per_cent['ВТБ'])
profit_sber = int(user_money / 100 * per_cent['СБЕР'])
list_of_profit = [profit_tkb, profit_skb, profit_vtb, profit_sber]
print('Указанная Вами сумма: ' + str(user_money) + ' руб.')
print(f'{"Чистый доход (руб.) по банкам:"}\n{"ТКБ  СКБ  ВТБ  СБЕР"}\n{list_of_profit}')
print("Максимальный доход: " + str(max(list_of_profit)) + " руб.")
