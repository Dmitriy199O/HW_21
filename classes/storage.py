from abc import ABC, abstractmethod
from classes.exceptions import NoRequiredQuantity, NotFound


class Storage(ABC):
	"""Абстрактный класс для хранилища"""

	@abstractmethod
	def __init__(self, items={}, capacity=0):
		self._items = items
		self._capacity = capacity

	@abstractmethod
	def add(self, name: str, amount: int):
		"""Добавляет товары в хранилище"""
		pass

	def remove(self, name: str, amount: int):
		"""Удаляет товары из хранилища"""
		if name not in self._items:
			raise NotFound(f'Товар "{name}" не найден')

		if self._items[name] > amount:
			self._items[name] -= amount
		elif self._items[name] == amount:
			del self._items[name]
		else:
			raise NoRequiredQuantity('Нужного количества нет на складе')

	def get_free_space(self) -> int:
		"""Возвращает свободное место"""
		amount = sum(self._items.values())
		return self._capacity - amount

	@property
	def get_items(self) -> dict:
		"""Возвращает список товаров"""
		return self._items

	def get_unique_items(self) -> int:
		"""Возвращает кол-во уникальных элементов"""
		return len(self._items)
