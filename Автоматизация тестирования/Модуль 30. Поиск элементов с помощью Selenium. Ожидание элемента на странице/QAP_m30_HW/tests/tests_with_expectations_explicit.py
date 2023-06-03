import pytest
# import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
	pytest.driver = webdriver.Chrome('./chromedriver.exe')
	pytest.driver.set_window_size(1366, 768)
	# Переходим на страницу авторизации
	pytest.driver.get('http://petfriends.skillfactory.ru/login')

	yield

	pytest.driver.quit()


def test_check_all_pets_explicit():
	pytest.driver.find_element('id', 'email').send_keys('qa@test.com')
	pytest.driver.find_element('id', 'pass').send_keys('Qwerty123!!!')
	pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

	element = WebDriverWait(pytest.driver, 10).until(
		EC.presence_of_element_located((By.LINK_TEXT, "Мои питомцы"))
	)
	element.click()

	element_stat = pytest.driver.find_elements(By.XPATH, '//div[@class=".col-sm-4 left"]')
	element_pets_in_table = pytest.driver.find_elements(By.TAG_NAME, "tr")
	all_pets_in_table = len(element_pets_in_table) - 1

	# Проверка: 1. Присутствуют все питомцы
	for element in element_stat:
		text = element.text
		# Регулярка для поиска чисел в тексте
		numbers = re.findall(r'\d+', text)
		if numbers:
			assert int(numbers[0]) == all_pets_in_table, "Кол-во питомцев в статистике не равно питомцам в таблице"

	# Проверка: 2. Хотя бы у половины питомцев есть фото
	element_pets_in_table = pytest.driver.find_elements(By.TAG_NAME, "tr")
	all_pets_in_table = len(element_pets_in_table) - 1
	images = pytest.driver.find_elements(By.CSS_SELECTOR, "img[src]")
	count_images = len(images) - 1
	assert count_images >= all_pets_in_table * 0.5, "Количество питомцев с фото менее 50% от общего числа"

	# Проверка: 3. У всех питомцев есть имя, возраст и порода
	td_elements = pytest.driver.find_elements(By.TAG_NAME, "td")
	for td_element in td_elements:
		assert td_element.text, "Имя, порода или возраст не заполнены"

	# Проверка: 4. У всех питомцев разные имена
	td_elements = pytest.driver.find_elements(By.TAG_NAME, "td")
	# Список с именами питомцев
	my_list = []
	for i in range(0, len(td_elements), 4):
		my_list.append(td_elements[i].text)

	assert len(my_list) == len(set(my_list)), "В таблице есть питомцы с одинаковыми именами"
