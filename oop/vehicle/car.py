from . import Vehicle

class Car(Vehicle):

	brands = {
		'BMW': {'price': '$40,000', 'speed': '1000cc'}, 
		'LAMBO': {'price': '$50,000', 'speed': '1100cc'}, 
		'CIVIC': {'price': '$60,000', 'speed': '400cc'}, 
		'FERARI': {'price': '$80,000', 'speed': '2000cc'}
	}
	
	def get_price(self):

		if self._check_brand(self.brands) is False:
			return self.get_error_message()
		
		brand = self.brands[self.brand]

		if self.color not in brand['colors']:
			return "Unfortunely, the color \"" + self.color + "\" is empty"

		return brand['price']

	def how_fast(self):

		if self.__check_brand() is False:
			return self.get_error_message()
		


