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



# ----------

class Person:
    def __init__(self, name, age, ocupation):
        self._name = name.lower()
        self.age = age
        self._ocupation = ocupation.lower()
        
    def __str__(self):
        return f'{self._name} | {self.age} | {self._ocupation}'
            
    def birthday(self):
        self.age += 1
    
    @property
    def greeting(self):
        return f'Welcome my favorite {self._ocupation}'

person1 = Person('Caio', 19, 'Frontend Developer')

# print(person1)
# person1.greeting
# person1.birthday()
# print(person1)

# ----------



# ----------

class BankAccount:
    def __init__(self, holder, balance, active):
        self._holder = holder
        self._balance = balance
        self._active = active
        
    def __str__(self):
        return f'{self._holder} | {self._balance} | {self._active}'
    
    @property
    def active_account(self):
        self._active = not self._active

# ----------



# ----------

class Restaurant:
    restaurants = []
    
    def __init__(self, name, category):
        self._name = name.lower()
        self._category = category.lower()
        self._active = False
        Restaurant.restaurants.append(self)
        
    def __str__(self):
        return f'{self._name}, {self._category}'
    
    @classmethod
    def show_restaurant(cls):
        print(f'{'Name'.ljust(30)} | {'Category'.ljust(30)} | Status')
        for restaurant in cls.restaurants:
            print(f'{restaurant._name.ljust(30)} | {restaurant._category.ljust(30)} | {restaurant._active}')
            
    @property
    def active(self):
        return '1' if self._active else '0'
    
    def change_status(self):
        self._active = not self._active
    
# pizza_do_ze = Restaurant('Pizza do Ze', 'Pizzaria')
# sushi_do_mazuka = Restaurant('Sushi do Mazuka', 'Sushi')

# sushi_do_mazuka.change_status()
# Restaurant.show_restaurant()

# ----------
