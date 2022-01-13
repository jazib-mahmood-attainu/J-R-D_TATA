from random import choice
from entities.restaurant import Restaurant
class Customer:
    def show_restaurant(self):
        rest = Restaurant()
        for i in rest.dict_of_rests.keys():
            print(i)
        choice = input("Select from above or enter a dish name?(S/D)")
        if choice =="S":
            r = input("Select a restaurant(type it's name)")
            print("menu:")
            print({k: v for k, v in sorted(rest.dict_of_rests[r][0].items(), key=lambda item: item[1])})
        elif choice=="D":
            return
        else:
            print("give correct option")



    def order(self):
        self.show_restaurant()
        dish = input("Enter the dish required")
        print(dish)
        #dish search in menu of each restaurant
        #if dish is there show it, otherwise ask again for the dish

    