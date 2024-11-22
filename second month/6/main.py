# users = ["Dilshod", "Murtazoyev", 24, 2000]
#
#
# user = {
#     "name": "Dilshod",
#     "lastname": "Murtazoyev",
#     "age": 25,
#     "gender": "M",
#     "job": "Engineer",
#     "email": "dilshod@gmail.com",
#     "phone": "+1 9876543210",
#     "skills": ["python", "javascript", "HTML", "CSS", "ReactJS", "NodeJS", "NextJS"],
#     "isMarred": True,
# }
#
# user2 = user.copy()
#
# user2["lastname"] = "Murtazoyeeev"

# print(type(user), user["email"], user.values(), user.keys(), sep="\n")
# print(len(user), user2, sep="\n")

# print(users[0])

# ism = input("ismni kiriting")
#
# new_list = dict(name=f"{ism}", age=22, gender="Male")
# print(new_list)

# fruit = {
#     'name': "apple",
#     'color': "blue",
#     'weight': 100,
# }
#
# a = fruit.items()
#
# print(list(a)[0])

# fruit = {
#     'name': "apple",
#     'color': "blue",
#     'weight': 100,
# }

# print(
#     fruit.get("color"),
# )
#
#
# if "apple" in fruit.values():
#     print(True)
# else:
#     print(False)

# fruit.update({"weight": 200})
# fruit.update({"quantity": 120})
# fruit["price"] = 12_000_000

# fruit.pop("name")

# fruit.popitem()

# del fruit["weight"]
# del fruit

# print(fruit)

# fruit = {
#     'name': "apple",
#     'color': "blue",
#     'weight': 100,
# }

# apple = dict(fruit)
#
# apple['color'] = "red"
#
#
# print(apple, fruit, sep="\n")
#