from entities.restaurant import Restaurant
from entities.customer import Customer
def run():
    user_type = input("Are you a restaurant(R) registering or a customer buying food(C)")
    if user_type=="R":
        rest = Restaurant()
        rest.register()
    elif user_type=="C":
        cust = Customer()
        cust.order()
    else:
        print("Entered wrong choice, provide either R or C")

    print(rest.dict_of_rests)
if __name__=="__main__":
    run()