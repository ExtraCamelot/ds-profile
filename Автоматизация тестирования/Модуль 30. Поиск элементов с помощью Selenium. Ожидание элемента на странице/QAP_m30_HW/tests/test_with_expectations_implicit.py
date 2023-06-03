import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By



@pytest.fixture(autouse=True)
def testing():
	pytest.driver = webdriver.Chrome('./chromedriver.exe')
	pytest.driver.set_window_size(1366, 768)
	# Неявные ожидания
	pytest.driver.implicitly_wait(5)
	# Переходим на страницу авторизации
	pytest.driver.get('http://petfriends.skillfactory.ru/login')

	yield

	pytest.driver.quit()


def test_check_all_pets_implicit():
	pytest.driver.find_element('id', 'email').send_keys('qa@test.com')
	pytest.driver.find_element('id', 'pass').send_keys('Qwerty123!!!')
	pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
	myDynamicElement = pytest.driver.find_elements(By.ID, "myDynamicElement")

	img_loader = pytest.driver.find_elements(By.CSS_SELECTOR, "img[src]")
	name_loader = pytest.driver.find_elements(By.CSS_SELECTOR, "img[src]")
	name_loader = pytest.driver.find_elements(By.CLASS_NAME, "card-title")
	card_text_loader = pytest.driver.find_elements(By.CLASS_NAME, "card-text")

	# Хэдер страницы
	header = pytest.driver.find_elements(By.XPATH, '//nav')

	# Лого в header
	logo = pytest.driver.find_elements(By.XPATH, '//a[@class="navbar-brand header2"]')

	# Пункты меню
	menu = pytest.driver.find_elements(By.XPATH, '//ul[@class="navbar-nav"]')

	# Кнопка «Выйти»
	exit_btn = pytest.driver.find_elements(By.XPATH, '//button[@class="btn btn-outline-secondary"]')

	# Заголовок страницы
	title = pytest.driver.find_elements(By.XPATH, '//h1[@class="text-center"]')

	# Карточки питомцев (все 100)
	title = pytest.driver.find_elements(By.XPATH, '//div[@class="card"]')

	# Фото питомцев (все 100)
	title = pytest.driver.find_elements(By.XPATH, '//img')

	# Имена питомцев (все 100)
	title = pytest.driver.find_elements(By.XPATH, '//h5[@class="card-title"]')

	# Возраст питомцев и порода (все 100)
	title = pytest.driver.find_elements(By.XPATH, '//p[@class="card-text"]')
