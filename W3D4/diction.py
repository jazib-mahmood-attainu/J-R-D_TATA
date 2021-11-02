#dictionaries
# d = {
#         "key1":25,
#         "key2":"Hyderabad",
#         "key3":[8,5,6,3,9,8,3,9,1,8],
#     }

# print(type(d))

# print(d["key2"][2:6])

hometown_students = {
                        "sudhakar":"Bhubaneswar",
                        "Aniket":"Gwalior",
                        "Brian":"Mangalore",
                        "Imran":"Delhi",
                        "Jazib":"Gorakhpur",

                    }


print(hometown_students["Jazib"])
#updating dictionary
hometown_students["Jazib"] = "Lucknow" 

print(hometown_students)
#inserting a key value pair in a dictionary
hometown_students["mahesh"] = "Vijaywada"

print(hometown_students)
#deleting value pair in a dictionary
hometown_students.pop("Jazib")

print(hometown_students)

print(hometown_students.keys())

print(hometown_students.values())

for k in hometown_students.keys():
    print(k,"'s hometown is",hometown_students[k])




