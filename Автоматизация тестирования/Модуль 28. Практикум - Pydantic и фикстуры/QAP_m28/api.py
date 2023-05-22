import requests


class AccessTokenRequest:
	def __init__(self):
		self.base_url = "https://restful-booker.herokuapp.com/"

	# POST - GET TOKEN
	def get_token(self, username, password):
		res = requests.post(self.base_url + 'auth', data={'username': username, 'password': password})
		status = res.status_code
		result = ""
		try:
			result = res.json()
		except:
			result = res.text
		return status, result

	# GET - GET Booking Ids
	def get_booking_ids(self, params_filter):
		params_filter = params_filter
		res = requests.get(self.base_url+'booking', params=params_filter)
		status = res.status_code
		result = ""
		try:
			result = res.json()
		except:
			result = res.text
		return status, result


acc_token = AccessTokenRequest()
