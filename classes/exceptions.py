class NotFound(Exception):
	"""Товар не найден"""
	pass


class StorageFull(Exception):
	"""Хранилище заполнено"""
	pass


class MaxUnique(Exception):
	"""Превышен лимит уникальных товаров"""
	pass


class NoRequiredQuantity(Exception):
	"""Нет достаточного кол-ва товара в хранилище"""
	pass
