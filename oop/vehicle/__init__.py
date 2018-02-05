class Vehicle:

	_error_message = ''

	def __init__(self, brand, color):
		self.brand = brand
		self.color = color

	def set_error_message(self, text):
		self._error_message = text

	def get_error_message(self):
		return self._error_message

	def _check_brand(self, brands):
		if self.brand in brands:
			return True
		else:
			self.set_error_message("Brand \"" + self.brand + "\" is not found")
			return False
