import pytest
from app.calculator import Calculator


class TestCalc:
	# Подготовительный метод, в котором создаётся объект калькулятора из импортированного класса Calculator
	def setup(self):
		self.calc = Calculator

	# Тесты
	# Позитивная проверка функции умножения приложения Calculator
	def test_multiply_calculate_correctly(self):
		# assert служит для сравнивания ожидания с результатом (это метод библиотеки PyTest)
		assert self.calc.multiply(self, 2, 4) == 8

	# Негативная проверка функции умножения приложения Calculator
	def test_multiply_calculate_failed(self):
		assert self.calc.multiply(self, 2, 4) == 7

	# Задание 19.2.3 - позитивные проверки для методов приложения Calculator
	def test_multiply_positive(self):
		assert self.calc.multiply(self, 1, 4) == 4

	def test_devision_positive(self):
		assert self.calc.devision(self, 33, 3) == 11

	def test_subtraction_positive(self):
		assert self.calc.subtraction(self, 20, 10) == 10

	def test_adding_positive(self):
		assert self.calc.adding(self, 0, 1) == 1
