from . import Vehicle

class Motorcycle(Vehicle):
	
	brands = {
		'YAMAHA': {'price': '$1200', 'colors': [ 'White', 'Black', 'Blue']},
		'HONDA': {'price': '$1300', 'colors': ['Red', 'Orange']},
		'SUZUKI': {'price': '$1230', 'colors': ['Gray', 'Blue']},
	}

	def get_price(self):

		if self._check_brand(self.brands) is False:
			return self.get_error_message()

		brand = self.brands[self.brand]

		if self.color not in brand['colors']:
			return "Unfortunely, the color \"" + self.color + "\" is empty"

		return brand['price']

	def show_colors_provided(self):

		if self._check_brand(self.brands) is False:
			return self.get_error_message()

		return self.brands[self.brand]['colors']
