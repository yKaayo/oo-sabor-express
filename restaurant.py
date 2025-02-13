class Restaurant:
    name = ''
    category = ''
    active = False
    
pizzaDoZe = Restaurant()
pizzaDoZe.name = 'Pizza do Ze'
pizzaDoZe.category = 'Pizzaria'

print(vars(pizzaDoZe))
print(pizzaDoZe.name)

# ----------------

class Music:
    name = ''
    artist = ''
    duration = int
    
trapMusic = Music()
trapMusic.name = 'Massive'
trapMusic.artist = 'Drake'
trapMusic.duration = 200
