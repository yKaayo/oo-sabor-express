from models.restaurant import Restaurant

pizza_do_ze = Restaurant('Pizza do Ze', 'Pizzaria')
pizza_do_ze.get_rating('Caio', 10)
pizza_do_ze.get_rating('Pao', 2)

def main():
    Restaurant.show_restaurant()

if __name__ == '__main__':
    main()