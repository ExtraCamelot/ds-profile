import pytest
from api import acc_token
from pydantic_models.p_models import Authorization, NegativeAuthorization, FilterForId


# Тест 1: получение токена, валидные данные
@pytest.mark.parametrize("username", [
	'admin'
], ids=[
	'POSITIVE TEST - username'
])
@pytest.mark.parametrize("password", [
	'password123'
], ids=[
	'POSITIVE TEST - password'
])
def test_get_token(username, password):
	status, result = acc_token.get_token(username, password)
	try:
		assert status == 200
		assert 'token' in result
		res_data = Authorization.parse_obj(result)
		assert type(res_data.token) is str
		print('\n', status, result, res_data)
	except ValueError as e:
		print("Pydantic Exception", e.json())


# Тест 2: получение токена, невалидные данные логина
@pytest.mark.parametrize("username", [
	'ADMIN',
	'AdMiN',
	'AdM1N',
	'ad min',
	' admin',
	'admin ',
	' ',
	''
], ids=[
	'NEGATIVE TEST - username: upper case',
	'NEGATIVE TEST - username: upper & lower case',
	'NEGATIVE TEST - username: upper & lower case with digit',
	'NEGATIVE TEST - username: lower case with whitespace',
	'NEGATIVE TEST - username: whitespace at the beginning',
	'NEGATIVE TEST - username: whitespace at the end',
	'NEGATIVE TEST - username: only one whitespace',
	'NEGATIVE TEST - username: null',
])
@pytest.mark.parametrize("password", [
	'password123'
], ids=[
	'POSITIVE TEST - password'
])
def test_get_token_invalid_login(username, password):
	status, result = acc_token.get_token(username, password)
	try:
		assert status == 200
		assert 'reason' in result
		res_data = NegativeAuthorization.parse_obj(result)
		assert res_data.reason == 'Bad credentials'
		print('\n', status, result, res_data)
	except ValueError as e:
		print("Pydantic Exception", e.json())


# Тест 3: получение токена, невалидные данные пароля
@pytest.mark.parametrize("password", [
	'PASSWORD123',
	'PaSsWoRd123',
	'password321',
	'password 123',
	' password123',
	'password123 ',
	' ',
	''
], ids=[
	'NEGATIVE TEST - password: upper case',
	'NEGATIVE TEST - password: upper & lower case',
	'NEGATIVE TEST - password: with different digits',
	'NEGATIVE TEST - password: lower case with whitespace',
	'NEGATIVE TEST - password: whitespace at the beginning',
	'NEGATIVE TEST - password: whitespace at the end',
	'NEGATIVE TEST - password: only one whitespace',
	'NEGATIVE TEST - password: null',
])
@pytest.mark.parametrize("username", [
	'admin'
], ids=[
	'POSITIVE TEST - username'
])
def test_get_token_invalid_password(username, password):
	status, result = acc_token.get_token(username, password)
	try:
		assert status == 200
		assert 'reason' in result
		res_data = NegativeAuthorization.parse_obj(result)
		assert res_data.reason == 'Bad credentials'
		print('\n', status, result, res_data)
	except ValueError as e:
		print("Pydantic Exception", e.json())


# Тест 4: получение списка id гостей - без фильтра
@pytest.mark.parametrize("params_filter", [
	{'': ''}
], ids=[
	'POSITIVE TEST - empty filter'
])
def test_get_booking_ids(params_filter):
	status, result = acc_token.get_booking_ids(params_filter)
	try:
		ids = [FilterForId(**ids) for ids in result]
		assert len(ids) > 0
		assert type(ids[0].bookingid) is int
		print('\n', status, result)
	except ValueError as e:
		print("Pydantic Exception", e.json())


# Тест 5: получение списка id гостей - фильтр firstname, валидные данные
@pytest.mark.parametrize("params_filter", [
	{'firstname': 'John'},
	{'firstname': 'Jim'},
	{'firstname': 'Mary'},
	{'firstname': 'Eric'}
], ids=[
	'POSITIVE TEST - valid firstname',
	'POSITIVE TEST - valid firstname',
	'POSITIVE TEST - valid firstname',
	'POSITIVE TEST - valid firstname'
])
def test_get_booking_ids_firstname(params_filter):
	status, result = acc_token.get_booking_ids(params_filter)
	try:
		ids = [FilterForId(**ids) for ids in result]
		assert len(ids) > 0
		assert type(ids[0].bookingid) is int
		print('\n', status, result)
	except ValueError as e:
		print("Pydantic Exception", e.json())


# Тест 6: получение списка id гостей - фильтр firstname, невалидные данные
@pytest.mark.parametrize("params_filter", [
	{'firstname': ''},
	{'firstname': 123},
	{'firstname': '!@#$%^&*()'},
	{'firstname': 'JOHN'},
	{'firstname': 'JoHn'}
], ids=[
	'NEGATIVE TEST - empty firstname',
	'NEGATIVE TEST - digits in firstname',
	'NEGATIVE TEST - spec symbols in firstname',
	'NEGATIVE TEST - valid name with UPPERCASE in firstname',
	'NEGATIVE TEST - valid name with CaMeLcAsE in firstname'
])
def test_get_booking_ids_invalid_firstname(params_filter):
	status, result = acc_token.get_booking_ids(params_filter)
	try:
		assert status == 200
		ids = [FilterForId(**ids) for ids in result]
		assert len(ids) == 0
		print('\n', status, result)
	except ValueError as e:
		print("Pydantic Exception", e.json())


# Тест 7: получение списка id гостей - фильтр lastname, валидные данные
@pytest.mark.parametrize("params_filter", [
	{'lastname': 'Brown'},
	{'lastname': 'Wilson'},
	{'lastname': 'Smith'},
	{'lastname': 'Jackson'}
], ids=[
	'POSITIVE TEST - valid lastname',
	'POSITIVE TEST - valid lastname',
	'POSITIVE TEST - valid lastname',
	'POSITIVE TEST - valid lastname'
])
def test_get_booking_ids_lastname(params_filter):
	status, result = acc_token.get_booking_ids(params_filter)
	try:
		ids = [FilterForId(**ids) for ids in result]
		assert len(ids) > 0
		assert type(ids[0].bookingid) is int
		print('\n', status, result)
	except ValueError as e:
		print("Pydantic Exception", e.json())


# Тест 8: получение списка id гостей - фильтр lastname, невалидные данные
@pytest.mark.parametrize("params_filter", [
	{'lastname': ''},
	{'lastname': 123},
	{'lastname': '!@#$%^&*()'},
	{'lastname': 'JACKSON'},
	{'lastname': 'JaCkSoN'}
], ids=[
	'NEGATIVE TEST - empty lastname',
	'NEGATIVE TEST - digits in lastname',
	'NEGATIVE TEST - spec symbols in lastname',
	'NEGATIVE TEST - valid name with UPPERCASE in lastname',
	'NEGATIVE TEST - valid name with CaMeLcAsE in lastname'
])
def test_get_booking_ids_invalid_lastname(params_filter):
	status, result = acc_token.get_booking_ids(params_filter)
	try:
		assert status == 200
		ids = [FilterForId(**ids) for ids in result]
		assert len(ids) == 0
		print('\n', status, result)
	except ValueError as e:
		print("Pydantic Exception", e.json())


# Тест 9: получение списка id гостей - парный фильтр firstname & lastname, валидные данные
@pytest.mark.parametrize("params_filter", [
	{
		'firstname': 'John',
		'lastname': 'Smith'
	},
	{
		'firstname': 'Eric',
		'lastname': 'Ericsson'
	}
], ids=[
	'POSITIVE TEST - valid firstname & lastname',
	'POSITIVE TEST - valid firstname & lastname'
])
def test_get_booking_ids_firstname_and_lastname(params_filter):
	status, result = acc_token.get_booking_ids(params_filter)
	try:
		ids = [FilterForId(**ids) for ids in result]
		assert len(ids) > 0
		assert type(ids[0].bookingid) is int
		print('\n', status, result)
	except ValueError as e:
		print("Pydantic Exception", e.json())


# Тест 10: получение списка id гостей - парный фильтр firstname & lastname, невалидные данные
@pytest.mark.parametrize("params_filter", [
	{
		'firstname': 'Джон',
		'lastname': 'Смит'
	},
	{
		'firstname': 'Ericsson',
		'lastname': 'Eric'
	}
], ids=[
	'NEGATIVE TEST - invalid firstname & lastname - Cyrillic',
	'NEGATIVE TEST - valid firstname & lastname - swap first and last names'
])
def test_get_booking_ids_firstname_and_lastname(params_filter):
	status, result = acc_token.get_booking_ids(params_filter)
	try:
		assert status == 200
		ids = [FilterForId(**ids) for ids in result]
		assert len(ids) == 0
		print('\n', status, result)
	except ValueError as e:
		print("Pydantic Exception", e.json())
