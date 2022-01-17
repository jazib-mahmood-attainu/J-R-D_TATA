class Driver:
    def __init__(self) -> None:
        self.dict_of_drivers = {
                            "Ali":{"model":"Swift","location":[0,0],"avail":True},
                            "Jazib":{"model":"Swift","location":[0,0],"avail":True},
                            "Sourav":{"model":"Swift","location":[0,0],"avail":True},
                              }
    def register(self):
        
        
        wish = True
        
        while True:
            if wish==False:
                break
            name = input("Enter Driver name")
            self.dict_of_drivers[name] = dict()
            model = input("Enter model name")
            location = list(map(int,input("Enter location by 2 coordinates").split()))
            avail = input("Enter availability(Y/N)?")
            self.dict_of_drivers[name]["model"] = model
            self.dict_of_drivers[name]["location"] = location
            if avail == "Y":
                self.dict_of_drivers[name]["avail"] = True
            elif avail == "N":
                self.dict_of_drivers[name]["avail"] = True
            else:
                print("give Y or N")

            
            
            choice = input("Do you want to register another Driver?(T/F)")
            
            if choice == "T":
                continue
            else:
                wish=False

        print(self.dict_of_drivers)

    

    def update(self,name):
        print(f"Menu ->{self.dict_of_rests[name][0]} has processing capacity of {self.dict_of_rests[name][1]}")
        choice = input("Update menu(M) or processing capacity(P)?(M/P)")
        if choice=="M":
            print(self.dict_of_rests[name][0])
            choice2 = input("Want to delete an item?(Y/N)")
            if choice2=="Y":
                item = input("Enter the item")
                self.dict_of_rests[name][0].pop(item)
            elif choice2=="N":
                item = input("Enter the item")
                price = input("Enter the price")
                self.dict_of_rests[name][0][item] = price
        elif choice=="P":
            pass
        else:
            print("enter correct choice")