from classes.exceptions import *
from classes.storage import Storage


class Shop(Storage):
	"""Класс магазина"""

	def __init__(self, items={}, capacity=20, unique=5):
		self._items = items
		self._capacity = capacity
		self._unique = unique
		

	def add(self, name: str, amount: int):
		"""Добавляет товары в магазин"""
		if self.get_free_space() < amount:
			raise StorageFull('Свободного места меньше, чем кол-во товара')
		elif name not in self._items and self.get_unique_items() >= self._unique:
			raise MaxUnique('Превышен лимит уникальных товаров')

		self._items[name] = self._items.get(name, 0) + amount
