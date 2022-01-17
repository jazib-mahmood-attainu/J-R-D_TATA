from entities.Rider import Rider
from entities.driver import Driver
def run():
    user_type = input("Are you a Driver(D) registering/update or a Rider booking Cab(R)")
    if user_type=="D":
        drvr = Driver()
        reg_upd = input("Are you a Driver(R) registering or updating(U) their location?(R/U)")
        if reg_upd=="R":
            drvr.register()
        elif reg_upd=="U":
            for i in drvr.dict_of_rests.keys():
                print(i)
            name = input("Enter restaurant name: ")
            drvr.update(name)
        else:
            print("enter correct choice")
        

    elif user_type=="R":
        location = list(map(int,input("Enter your location by 2 coordinates").split()))
        rdr = Rider()
        rdr.show_avail_cabs(location)
    else:
        print("Entered wrong choice, provide either D or R")

if __name__=="__main__":
    run()