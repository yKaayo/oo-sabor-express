# ----------

class Music:
    name = ''
    artist = ''
    duration = int
    
trapMusic = Music()
trapMusic.name = 'Massive'
trapMusic.artist = 'Drake'
trapMusic.duration = 200

# ----------

class Restaurant:
    restaurants = []
    
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.active = False
        Restaurant.restaurants.append(self)
        
    def __str__(self):
        return f'{self.name}, {self.category}'
    
    def show_restaurant():
        for restaurant in Restaurant.restaurants:
            print(f'{restaurant.name}, {restaurant.category}, {restaurant.active}')
    
pizzaDoZe = Restaurant('Pizza do Ze', 'Pizzaria')

Restaurant.show_restaurant()
