from classes.exceptions import *
from classes.request import Request
from classes.shop import Shop
from classes.store import Store


def main():
	# Обрабатываем запрос
	try:
		request = Request(input('Запрос: ')).get_request()
		from_ = request.get('from')
		to = request.get('to')
		amount = request.get('amount')
		product = request.get('product')
	except (TypeError, ValueError, IndexError):
		print('Проверьте правильность запроса')
		return ''

	# Ищем нужное кол-во на складе
	try:
		store.remove(product, amount)
		print(f'\nНужное количество есть в "{from_}"')
	except (StorageFull, NoRequiredQuantity, NotFound) as error:
		print(error)
		return ''

	# Доставляем в магазин
	try:
		shop.add(product, amount)
		print(f'Курьер забрал {amount} "{product}" из "{from_}" и везет в "{to}"')
		print(f'Курьер доставил {amount} "{product}" в "{to}"')
	except (StorageFull, MaxUnique) as error:
		print(error)
		return ''

	# Выводим кол-во товаров на складе и в магазине
	print(f'\nВ "{from_}" хранится:')
	for k, v in store.get_items.items():
		print(f' - {k}: {v}')
	print(f'Свободного места осталось: {store.get_free_space()}')
	print(f'\nВ "{to}" хранится:')
	for k, v in shop.get_items.items():
		print(f' - {k}: {v}')
	print(f'Свободного места осталось: {shop.get_free_space()}')


# Запускаем программу
test_store = {
		'печеньки': 10,
		'water': 20,
		'coca-cola': 10,
		'fanta': 10,
		'juice': 10,
		'7up': 10,
			}
store = Store(items=test_store)
shop = Shop()
print(
	'Приветствую, дорогой друг! Что и куда будем доставлять?\n'
    'Запрос должен быть вида: "Доставить <кол-во> <товар> из <откуда> в <куда>"'
	'\n(для тестирования можно просто указать кол-во и название (см. класс Request))'
	)
while shop.get_free_space() > 0:
	main()
	print('-' * 30)
print('В магазине не осталось свободного места!')
