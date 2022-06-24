class Request:
	"""Класс запроса"""

	def __init__(self, request: str):  # Доставить 3 печеньки из склад в магазин
		"""Для тестирования упрощен ввод"""
		self._request = request.split()
		self._from_ = 'склад'  # self._request[4]
		self._to = 'магазин'  # self._request[6]
		self._amount = int(self._request[0])  # int(self._request[1])
		self._product = self._request[1]  # self._request[2]

	def get_request(self) -> dict:
		return {
			'from': self._from_,
			'to': self._to,
			'amount': self._amount,
			'product': self._product,
		}
