def greet():
    print("Hello students")
    print("Welcome to TATA batch")
    print("Some text")


#sum of cube of numbers from 1 to n
# def sum_of_cubes(n):
    
#     s = 0
#     for i in range(1,n+1):
#         s += i**3 #s = s + i**3
#     return s

# n = int(input("Enter value of n"))
# res = sum_of_cubes(n) #225



# def add(a,b):
#     s = a+b
#     return s


# res = add(3,2)

# print(res)


# def star(n):
#     for row in range(1,n+1):
#         for stars in range(row):
#             print('*',end = " ")
#         print()


# star(15)

# def star(n):
    # lin =1
    # while lin<=n:
    #     no_of_stars = 0
    #     while no_of_stars<lin:
    #         print("*",end = " ")
    #         no_of_stars += 1
    #     print()
    #     lin+=1

# star(3)


# def star(n):
#     for line in range(1,n+1):#[1, 2, 3]
#         print("* "*line)
# star(3)
def temp_converter(temp_celcius):
    temp = (temp_celcius*9/5)+32
    return temp

country = input("Enter country")
temp_celcius = 32
if country == "usa":
    ans = temp_converter(temp_celcius)
    print("Temperature is ", ans,"degree Fahrenhiet")
else:
    print("Temperature is ", temp_celcius,"degree Celcius")