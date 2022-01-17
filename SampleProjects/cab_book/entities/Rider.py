from random import choice
from entities.driver import Driver
import math
class Rider:
    def show_avail_cabs(self,location):
        drvr = Driver()
        for i in drvr.dict_of_drivers.keys():
            if drvr.dict_of_drivers[i]["avail"]==True:
                dist = math.sqrt((drvr.dict_of_drivers[i]["location"][0]-location[0])**2+(drvr.dict_of_drivers[i]["location"][1]-location[1])**2)
                print(i,drvr.dict_of_drivers[i]["model"],"is at",dist,"meters")
        choice = input("Select from name of driver from above:")
        print(drvr.dict_of_drivers[choice.strip()], "is booked for you")
            
        



    def order(self):
        self.show_restaurant()
        dish = input("Enter the dish required")
        print(dish)
        #dish search in menu of each restaurant
        #if dish is there show it, otherwise ask again for the dish

    