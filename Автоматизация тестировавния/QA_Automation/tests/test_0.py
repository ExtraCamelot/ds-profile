# # Задание 19.2.--
# импорт библиотеки
import pytest
# из папки module_19 приложения calculator.py импортировать класс Calculator
from m_19.calculator import Calculator


# название класса должно обязательно начинаться со слова Test
class TestCalc:
	def setup(self):
		# определение подготовительного метода, в котором будет создаваться объект калькулятора из импортированного класса
		self.calc = Calculator

	# ТЕСТЫ (они также должны начинаться со слова test)
	# эта функция проверяет функцию умножения в классе Calculator (позитив)
	def test_multiply_calculate_correctly(self):
		# assert проверяет, что функция multiply при умножении 2 на 2 получит 4
		assert self.calc.multiply(self, 2, 2) == 4

	# Позитивные тесты для каждого метода калькулятора
	def test_dev_calculate_correctly(self):
		assert self.calc.devision(self, 2, 2) == 1

	def test_sub_calculate_correctly(self):
		assert self.calc.subtraction(self, 2, 2) == 0

	def test_add_calculate_correctly(self):
		assert self.calc.adding(self, 2, 2) == 4

	# эта функция проверяет функцию умножения в классе Calculator (негатив)
	def test_multiply_calculation_failed(self):
		# assert проверяет, что функция multiply при умножении 2 на 2 получит 5
		assert self.calc.multiply(self, 2, 2) == 5
