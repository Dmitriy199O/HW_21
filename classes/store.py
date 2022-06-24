from classes.storage import Storage
from classes.exceptions import *


class Store(Storage):
	"""Класс склада"""

	def __init__(self, items={}, capacity=100):
		self._items = items
		self._capacity = capacity

	def add(self, name: str, amount: int):
		"""Добавляет товары на склад"""
		if self.get_free_space() < amount:
			raise StorageFull('Свободного места меньше, чем кол-во товара')
		self._items[name] = self._items.get(name, 0) + amount
