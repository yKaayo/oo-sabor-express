from models.rating import Rating

class Restaurant:
    restaurants = []
    
    def __init__(self, name, category):
        self._name = name.lower()
        self._category = category.lower()
        self._active = False
        self._rating = []
        Restaurant.restaurants.append(self)
        
    def __str__(self):
        return f'{self._name}, {self._category}'
    
    @classmethod
    def show_restaurant(cls):
        print(f'{'Name'.ljust(20)} | {'Category'.ljust(20)} | {'Rating'.ljust(20)} | Status')
        for restaurant in cls.restaurants:
            print(f'{restaurant._name.ljust(20)} | {restaurant._category.ljust(20)} | {restaurant.mean_rating.ljust(20)} | {restaurant._active}')
            
    @property
    def active(self):
        return '1' if self._active else '0'
    
    def change_status(self):
        self._active = not self._active

    def get_rating(self, client, rate):
        rating = Rating(client, rate)
        self._rating.append(rating)

    @property
    def mean_rating(self):
        return str(round(sum(rating._rate for rating in self._rating) / len(self._rating), 1)) if self._rating else 0

    
# sushi_do_mazuka.change_status()
# Restaurant.show_restaurant()
