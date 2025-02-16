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

class Book:
    books = []

    def __init__(self, title, author, release_publication):
        self._title = title
        self._author = author
        self._release_publication = release_publication
        self._available = True
        Book.books.append(self)

    def __str__(self):
        return f'{self._title.ljust(20)} | {self._author.ljust(20)} | {self._release_publication}'
    
    @property
    def set_available(self):
        self._available = not self._available
        print(self._available)
        return self._available

book1 = Book('Micro-Hábitos', 'B. J. Fogg', 2020)
# book1.set_available

book2 = Book('A Única Coisa', 'Gary Keller', 2021)

# print(book1)
# print(book2)

# ----------
