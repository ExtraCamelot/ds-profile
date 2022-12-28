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


line_coordinates = ['0', 'A', 'B', 'C']
line_one = ['1', '-', '-', '-']
line_two = ['2', '-', '-', '-']
line_tree = ['3', '-', '-', '-']

motion_history = []

while True:
	def game_field():
		print(*line_coordinates)
		print(*line_one)
		print(*line_two)
		print(*line_tree)

	def choise_of_gamer (ch, player):
		if player == 1:
			if ch == 'A1':
				line_one[1] = 'X'
			elif ch == 'A2':
				line_two[1] = 'X'
			elif ch == 'A3':
				line_tree[1] = 'X'
			elif ch == 'B1':
				line_one[2] = 'X'
			elif ch == 'B2':
				line_two[2] = 'X'
			elif ch == 'B3':
				line_tree[2] = 'X'
			elif ch == 'C1':
				line_one[3] = 'X'
			elif ch == 'C2':
				line_two[3] = 'X'
			elif ch == 'C3':
				line_tree[3] = 'X'
		else:
			if ch == 'A1':
				line_one[1] = '0'
			elif ch == 'A2':
				line_two[1] = '0'
			elif ch == 'A3':
				line_tree[1] = '0'
			elif ch == 'B1':
				line_one[2] = '0'
			elif ch == 'B2':
				line_two[2] = '0'
			elif ch == 'B3':
				line_tree[2] = '0'
			elif ch == 'C1':
				line_one[3] = '0'
			elif ch == 'C2':
				line_two[3] = '0'
			elif ch == 'C3':
				line_tree[3] = '0'



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

	def check_for_victory():
		l_one, l_two, l_tree = ''.join(line_one), ''.join(line_two), ''.join(line_tree)
		if l_one == '1XXX' or l_two == '2XXX' or l_tree == '3XXX' \
				or (line_one[1] == 'X' and line_two[1] == 'X' and line_tree[1] == 'X')\
				or (line_one[2] == 'X' and line_two[2] == 'X' and line_tree[2] == 'X')\
				or (line_one[3] == 'X' and line_two[3] == 'X' and line_tree[3] == 'X')\
				or (line_one[1] == 'X' and line_two[2] == 'X' and line_tree[3] == 'X')\
				or (line_one[3] == 'X' and line_two[2] == 'X' and line_tree[1] == 'X'):
			print('Победа Игрока 1. Поздравляем!')
			return True
		elif l_one == '1000' or l_two == '2000' or l_tree == '3000' \
				or (line_one[1] == '0' and line_two[1] == '0' and line_tree[1] == '0')\
				or (line_one[2] == '0' and line_two[2] == '0' and line_tree[2] == '0')\
				or (line_one[3] == '0' and line_two[3] == '0' and line_tree[3] == '0')\
				or (line_one[1] == '0' and line_two[2] == '0' and line_tree[3] == '0')\
				or (line_one[3] == '0' and line_two[2] == '0' and line_tree[1] == '0'):
			print('Победа Игрока 2. Поздравляем!')
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
	if check_for_victory() == True:
		input('Для выхода из приложения нажмите Enter:')
		break
	gamer_motion(2)
	game_field()
	if check_for_victory() == True:
		input('Для выхода из приложения нажмите Enter:')
		break