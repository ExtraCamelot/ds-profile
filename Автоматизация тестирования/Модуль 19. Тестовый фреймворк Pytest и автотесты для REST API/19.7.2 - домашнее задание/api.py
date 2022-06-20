# библиотека запросов
import requests
# библиотека смешанных запросов
from requests_toolbelt.multipart.encoder import MultipartEncoder

import json


class PetFriends:
	def __init__(self):
		self.base_url = "https://petfriends.skillfactory.ru/"

	# GET - API KEY
	def get_api_key(self, email, password):
		headers = {
			'email': email,
			'password': password
		}
		res = requests.get(self.base_url+'api/key', headers=headers)
		status = res.status_code
		result = ""
		try:
			result = res.json()
		except:
			result = res.text
		return status, result

	# GET - PET LIST
	def get_list_of_pets(self, auth_key, filter):
		headers = {'auth_key': auth_key['key']}
		filter = {'filter': filter}

		res = requests.get(self.base_url+'api/pets', headers=headers, params=filter)
		status = res.status_code
		result = ""
		try:
			result = res.json()
		except:
			result = res.text
		return status, result

	# POST - NEW PET SIMPLE
	def add_new_pet_simple(self, auth_key, name, animal_type, age):
		# Обязательные заголовки
		headers = {'auth_key': auth_key['key']}
		res = requests.post(self.base_url+'/api/create_pet_simple', headers=headers, data={'name': name, 'animal_type': animal_type, 'age': age})
		status = res.status_code
		result = ""
		try:
			result = res.json()
		except:
			result = res.text
		return status, result

	# POST - NEW PET WITH PHOTO
	def add_new_pet(self, auth_key, name, animal_type, age, pet_photo):
		# Смешанные типы данных с помощью библиотеки requests_toolbelt
		data = MultipartEncoder(
			fields={
				'name': name,
				'animal_type': animal_type,
				'age': age,
				'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
			})
		# Обязательные заголовки
		headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

		res = requests.post(self.base_url+'api/pets', headers=headers, data=data)
		status = res.status_code
		result = ""
		try:
			result = res.json()
		except:
			result = res.text
		return status, result

	# PUT - Update information about pet
	def update_pet_info(self, auth_key, pet_id, name, animal_type, age) -> json:
		data = {
				'name': name,
				'animal_type': animal_type,
				'age': age,
			}
		# Обязательные заголовки
		headers = {'auth_key': auth_key['key']}

		res = requests.put(self.base_url+'api/pets/'+pet_id, headers=headers, data=data)
		status = res.status_code
		result = ""
		try:
			result = res.json()
		except json.decoder.JSONDecodeError:
			result = res.text
		return status, result

	# POST - Add photo of a pet
	def update_pet_photo(self, auth_key, pet_id, pet_photo):
		# Смешанные типы данных с помощью библиотеки requests_toolbelt
		data = MultipartEncoder(
			fields={
				'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
			})
		# Обязательные заголовки
		headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

		res = requests.post(self.base_url+'/api/pets/set_photo/'+pet_id, headers=headers, data=data)
		status = res.status_code
		result = ""
		try:
			result = res.json()
		except json.decoder.JSONDecodeError:
			result = res.text
		return status, result

	# DELETE - Delete pet from database
	def delete_pet_from_db(self, auth_key, pet_id):
		# Обязательные заголовки
		headers = {'auth_key': auth_key['key']}

		res = requests.delete(self.base_url+'api/pets/'+pet_id, headers=headers)
		status = res.status_code
		result = ""
		try:
			result = res.json()
		except:
			result = res.text
		return status, result
