print('Здравствуйте! Перед Вами народная игра "Крестики-нолики."\n'
	  'Игроки по очереди ставят на свободные клетки поля 3×3 знаки "X" или 0.\n'
	  'Выигрывает тот  игрок, который выстроит в ряд 3 своих знака по вертикали, горизонтали или диагонали.\n\n'
	  'ПРАВИЛА ИГРЫ:\n'
	  'Первый игрок играет крестиками. Участники должны опредлить, кто из них будет ходить первым.\n'
	  'Запись ходов осуществляется в виде координат. Например, если первый игрок ввел B2, то поле будет выглядеть так:\n')
print('0', 'A', 'B', 'C')
print('1', '-', '-', '-')
print('2', '-', 'X', '-')
print('3', '-', '-', '-')
print('\nПоехали!\n')

line_field = {'A1':'-', 'A2':'-', 'A3':'-', 'B1':'-', 'B2':'-', 'B3':'-', 'C1':'-', 'C2':'-', 'C3':'-',}
line_coordinates = ['0', 'A', 'B', 'C']
line_one = []
line_two = []
line_tree = []

motion_history = []

while True:
	def game_field():
		line_one = ['1', line_field['A1'], line_field['B1'], line_field['C1']]
		line_two = ['2', line_field['A2'], line_field['B2'], line_field['C2']]
		line_tree = ['3', line_field['A3'], line_field['B3'], line_field['C3']]
		print(*line_coordinates)
		print(*line_one)
		print(*line_two)
		print(*line_tree)

	def choise_of_gamer (ch, player):
		if player == 1:
			line_field[ch] = 'X'
		else:
			line_field[ch] = '0'

	def choise_logic(gamer_choise, player):
		if (gamer_choise in motion_history):
			print("Уже есть такой ход! Введите незанятую координату поля!")
			gamer_motion(player)
		else:
			if gamer_choise == 'A1' or gamer_choise == 'A2' or gamer_choise == 'A3' or gamer_choise == 'B1' or \
					gamer_choise == 'B2' or gamer_choise == 'B3' or gamer_choise == 'C1' or gamer_choise == 'C2' \
					or gamer_choise == 'C3':
				choise_of_gamer(gamer_choise, player)
				motion_history.append(gamer_choise)
			else:
				print('Координата должна состоять из буквы и числа! Например, "В1"')
				gamer_motion(player)

	def gamer_motion(player):
		if player == 1:
			gamer_1 = input("Игрок 1, Ваш ход: ")
			gamer_1 = gamer_1.upper()
			choise_logic(gamer_1, player)
		else:
			gamer_2 = input("Игрок 2, Ваш ход: ")
			gamer_2 = gamer_2.upper()
			choise_logic(gamer_2, player)

	def check_combinations(player):
		sym = 'X'
		if player == 1:
			sym = 'X'
		else:
			sym = '0'

		if (line_field['A1'] == sym and line_field['B1'] == sym and line_field['C1'] == sym) \
				or (line_field['A2'] == sym and line_field['B2'] == sym and line_field['C2'] == sym) \
				or (line_field['A3'] == sym and line_field['B3'] == sym and line_field['C3'] == sym) \
				or (line_field['A1'] == sym and line_field['A2'] == sym and line_field['A3'] == sym)\
				or (line_field['B1'] == sym and line_field['B2'] == sym and line_field['B3'] == sym)\
				or (line_field['C1'] == sym and line_field['C2'] == sym and line_field['C3'] == sym)\
				or (line_field['A1'] == sym and line_field['B2'] == sym and line_field['C3'] == sym)\
				or (line_field['C1'] == sym and line_field['B2'] == sym and line_field['A3'] == sym):
			print(f'Победа Игрока {player}. Поздравляем!')
			return True
		else:
				return False

	def check_for_victory(player):
		if check_combinations(player):
			return True
		elif len(motion_history) == 9:
			print('Ничья!')
			return True
		else:
			return False

	if motion_history == []:
		game_field()
	gamer_motion(1)
	game_field()
	if check_for_victory(1) == True:
		input('Для выхода из приложения нажмите Enter:')
		break
	gamer_motion(2)
	game_field()
	if check_for_victory(2) == True:
		input('Для выхода из приложения нажмите Enter:')
		break