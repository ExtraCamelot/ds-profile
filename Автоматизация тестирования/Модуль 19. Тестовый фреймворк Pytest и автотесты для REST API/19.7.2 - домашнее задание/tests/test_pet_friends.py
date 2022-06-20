# импорт библиотеки и данных пользователя
from api import PetFriends
from settings import valid_email, valid_password, invalid_email

# инициализация библиотеки
pf = PetFriends()


# ТЕСТЫ

# 1. GET API KEY (positive)
def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
	# полученные результаты сохраняются в переменные (вернётся две переменные, поэтому их надо
	# сохранить в две переменные
	status, result = pf.get_api_key(email, password)
	# проверка того, что статус равен 200
	assert status == 200
	# проверка того, что в ответе есть ключ key
	assert 'key' in result
	print('\n', status, result)


# 2. GET PET LIST (positive) - без фильтра (в ответе будут 100 карточек с портала)
def test_get_all_pets_with_valid_key(filter=''):
	# при запросе возвращаются status и result, если не нужна одна из переменных, то можно поставит "_" на её месте
	_, auth_key = pf.get_api_key(valid_email, valid_password)
	status, result = pf.get_list_of_pets(auth_key, filter)
	assert status == 200
	# проверка того что внутри массива pets есть карточки (одна или больше)
	assert len(result['pets']) > 0


# 3. ADD NEW PET SIMPLE (positive)
def test_add_new_pet_simple():
	_, auth_key = pf.get_api_key(valid_email, valid_password)
	status, result = pf.add_new_pet_simple(auth_key, name='Джей Эс', animal_type='котэ', age='28')
	assert status == 200
	print('\n', status, result)


# 4. ADD NEW PET with photo (positive)
def test_add_new_pet_with_photo():
	_, auth_key = pf.get_api_key(valid_email, valid_password)
	status, result = pf.add_new_pet(auth_key, name='Джей ЭS', animal_type='котэ', age='28',
									pet_photo=r'..\tests\images\JS.jpg')
	assert status == 200
	print('\n', status, result)


# 5. Update information about pet (positive)
def test_update_pet_info():
	_, auth_key = pf.get_api_key(valid_email, valid_password)
	_, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

	# Если список не пустой, то пробуем обновить имя, тип и возраст последнего созданного (первый в массиве)
	if len(my_pets['pets']) > 0:
		status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name='Джава', animal_type='кот',
											age='30')

		# Проверяем что статус ответа = 200 и выводим ответ
		assert status == 200
		print('\n', status, result)
	else:
		# если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
		raise Exception("There is no my pets")


# 6. Update pet photo (positive)
def test_update_pet_photo():
	_, auth_key = pf.get_api_key(valid_email, valid_password)
	_, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

	# Если список не пустой, то пробуем обновить фото последнего созданного (первый в массиве)
	if len(my_pets['pets']) > 0:
		status, result = pf.update_pet_photo(auth_key, my_pets['pets'][0]['id'], pet_photo=r'..\tests\images\start.jpg')
		# Проверяем что статус ответа = 200 и выводим ответ
		assert status == 200
		print('\n', status, result)
	else:
		# если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
		raise Exception("There is no my pets")


# 7. Delete pet from database (positive)
def test_delete_pet():
	_, auth_key = pf.get_api_key(valid_email, valid_password)
	_, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

	# Еслди список не пустой, то пробуем удалить последнего созданного (первый в массиве)
	if len(my_pets['pets']) > 0:
		status, result = pf.delete_pet_from_db(auth_key, my_pets['pets'][0]['id'])

		# Проверяем что статус ответа = 200 и выводим ответ
		assert status == 200
		print('\n', status, result)
	else:
		# если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
		raise Exception("There is no my pets")


# 8. GET API KEY - invalid_email (negative)
def test_get_api_key_for_invalid_user(email=invalid_email, password=valid_password):
	# полученные результаты сохраняются в переменные (вернётся две переменные, поэтому их надо
	# сохранить в две переменные
	status, result = pf.get_api_key(email, password)
	# проверка того, что статус равен 200
	assert status >= 400
	print('\n', status, result)


# 9. ADD NEW PET - long name (positive)
def test_add_new_pet_with_long_name():
	_, auth_key = pf.get_api_key(valid_email, valid_password)
	status, result = pf.add_new_pet_simple(auth_key, name='LRkKCt3mBg2NQoAk1RXQXXhZAqI5Hd74uvIWFvUblNP3FdbMzfhyK4OQ2'
														  'wqw8B0g67zxlYD1UYv5j42RzuQROe0dzOELuPRhnN2JDzcg38KXs4AsJ9'
														  '5JCoRQBIqNJ8m7AcznFjpcLubkB832Y8nwBlpgm9JMNrS5Qbl5Q6rMj54'
														  'QUHZjibaKbywEs6JJRDMrmn60h91pcVHtzDOlSC1MIWg0z0sA7zqZImH1'
														  'SEYtZwOQ6WbIL1IcF0VUWGelDCS', animal_type='котэ', age='28')
	assert status == 200
	print('\n', status, result)


# 10. ADD NEW PET - name with spec symbols (positive)
def test_add_new_pet_name_with_spec_symbols():
	_, auth_key = pf.get_api_key(valid_email, valid_password)
	status, result = pf.add_new_pet_simple(auth_key, name='☺☻♥♦♣♠•◘', animal_type='kitty', age='28')
	assert status == 200
	print('\n', status, result)


# 11. ADD NEW PET - long type (positive)
def test_add_new_pet_name_with_long_type():
	_, auth_key = pf.get_api_key(valid_email, valid_password)
	status, result = pf.add_new_pet_simple(auth_key, name='Ash', animal_type='LRkKCt3mBg2NQoAk1RXQXXhZAqI5Hd74uvIWFvUb'
																			 'lNP3FdbMzfhyK4OQ2wqw8B0g67zxlYD1UYv5j42R'
																			 'zuQROe0dzOELuPRhnN2JDzcg38KXs4AsJ95JCoRQ'
																			 'BIqNJ8m7AcznFjpcLubkB832Y8nwBlpgm9JMNrS5'
																			 'Qbl5Q6rMj54QUHZjibaKbywEs6JJRDMrmn60h91p'
																			 'cVHtzDOlSC1MIWg0z0sA7zqZImH1SEYtZwOQ6WbI'
																			 'L1IcF0VUWGelDCS', age='28')
	assert status == 200
	print('\n', status, result)


# 12. ADD NEW PET - type with spec symbols (positive)
def test_add_new_pet_type_with_spec_symbols():
	_, auth_key = pf.get_api_key(valid_email, valid_password)
	status, result = pf.add_new_pet_simple(auth_key, name='1IcF0V', animal_type='☺☻♥♦♣♠•◘', age='28')
	assert status == 200
	print('\n', status, result)


# 13. ADD NEW PET - long age (positive)
def test_add_new_pet_name_with_long_age():
	_, auth_key = pf.get_api_key(valid_email, valid_password)
	status, result = pf.add_new_pet_simple(auth_key, name='Ash', animal_type='LRkKC', age='28874646546546546465464'
																						  '55464654664646464464664'
																						  '45634674785678569897978'
																						  '76897896789768976897689'
																						  '67897689678976897697697'
																						  '76587856786578657865865')
	assert status == 200
	print('\n', status, result)


# 14. ADD NEW PET - age with spec symbols (positive)
def test_add_new_pet_age_with_spec_symbols():
	_, auth_key = pf.get_api_key(valid_email, valid_password)
	status, result = pf.add_new_pet_simple(auth_key, name='Ash', animal_type='LRkKC', age='☺☻♥♦♣♠•◘')
	assert status == 200
	print('\n', status, result)


# 15. ADD NEW PET with csv (negative)
def test_add_new_pet_with_photo_csv():
	_, auth_key = pf.get_api_key(valid_email, valid_password)
	status, result = pf.add_new_pet(auth_key, name='Джей ЭS', animal_type='котэ', age='28',
									pet_photo=r'..\tests\images\test_petfriends.csv')
	assert status == 200
	print('\n', status, result)


# 16. ADD NEW PET with photo png (negative)
def test_add_new_pet_with_photo_png():
	_, auth_key = pf.get_api_key(valid_email, valid_password)
	status, result = pf.add_new_pet(auth_key, name='Джей ЭS', animal_type='котэ', age='28',
									pet_photo=r'..\tests\images\QA.png')
	assert status == 200
	print('\n', status, result)
