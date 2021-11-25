while True:
	try:
		subsequence = input('Введите последовательность целых чисел через пробел: ')
		# 1. Перобразование последовательности в список
		subsequence = subsequence.split()
		user_input = subsequence  # Отдельно сохраняем вариант, введённый пользователем
		subsequence = list(map(int, subsequence))
		user_input =  list(map(int, user_input))
		user_number = int(input('Введите любое число включения его в состав последовательности: '))
		# 1.1 Проверка, является ли в вводённая последовательность числами
	except ValueError as error:
		print("Вы ввели недопустимые знаки при вводе числовой последовательности! Попробуйте ещё раз.")
	else:
		# Вставка пользовательского числа в последовательность
		subsequence.append(user_number)
		# 2. Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)
		def sorting_list():
			for i in range(1, len(subsequence)):
				x = subsequence[i]
				idx = i
				while idx > 0 and subsequence[idx-1] > x:
					subsequence[idx] = subsequence[idx-1]
					idx -= 1
				subsequence[idx] = x
			print('Последовательность, введённая пользователем: ')
			print(user_input)
			print('Последовательность, отсортированная в порядке возрастания (включено число пользователя): ')
			print(subsequence)
		sorting_list()
		# 3. Двоичный поиск позиций элементов, которые расположены по бокам от ввдённого пользователем числа
		print('Поиск позиций элементов, которые расположены по бокам от введённого пользователем числа...')
		arr_len = len(subsequence)
		last_index = arr_len -1
		def binary_search(array, element, left, right):
			if left > right:  # если левая граница превысила правую,
				return False  # значит элемент отсутствует
			middle = (right + left) // 2  # находимо середину
			if array[middle] == element:  # если элемент в середине,
				return middle  # возвращаем этот индекс
			elif element < array[middle]:  # если элемент меньше элемента в середине
				# рекурсивно ищем в левой половине
				return binary_search(array, element, left, middle - 1)
			else:  # иначе в правой
				return binary_search(array, element, middle + 1, right)
		# запускаем алгоритм на левой и правой границе
		# поиск индекса введённого пользователеми числа
		user_number_index = binary_search(subsequence, user_number, 0, last_index)
		if (user_number_index == 0):
			print('Число, введённое пользователем, является самым маленьким в последовательности! Его индекс: 0')
		elif (user_number_index == last_index):
			print('Число, введённое пользователем, является самым большим в последовательности! Его индекс: ' + str(last_index))
		else:
			print('Номер позиции близжайшего элемента (' + str(subsequence[user_number_index - 1]) + '), который меньше введенного пользователем числа: '
				  + str(user_number_index - 1))
			print('Номер позиции близжайшего элемента (' + str(subsequence[user_number_index + 1]) + '), который больше введенного пользователем числа: '
				  + str(user_number_index + 1))
		break