# # # users = ["Dilshod", "Murtazoyev", 24, 2000]
# # #
# # #
# # # user = {
# # #     "name": "Dilshod",
# # #     "lastname": "Murtazoyev",
# # #     "age": 25,
# # #     "gender": "M",
# # #     "job": "Engineer",
# # #     "email": "dilshod@gmail.com",
# # #     "phone": "+1 9876543210",
# # #     "skills": ["python", "javascript", "HTML", "CSS", "ReactJS", "NodeJS", "NextJS"],
# # #     "isMarred": True,
# # # }
# # #
# # # user2 = user.copy()
# # #
# # # user2["lastname"] = "Murtazoyeeev"
# #
# # # print(type(user), user["email"], user.values(), user.keys(), sep="\n")
# # # print(len(user), user2, sep="\n")
# #
# # # print(users[0])
# #
# # # ism = input("ismni kiriting")
# # #
# # # new_list = dict(name=f"{ism}", age=22, gender="Male")
# # # print(new_list)
# #
# # # fruit = {
# # #     'name': "apple",
# # #     'color': "blue",
# # #     'weight': 100,
# # # }
# # #
# # # a = fruit.items()
# # #
# # # print(list(a)[0])
# #
# # # fruit = {
# # #     'name': "apple",
# # #     'color': "blue",
# # #     'weight': 100,
# # # }
# #
# # # print(
# # #     fruit.get("color"),
# # # )
# # #
# # #
# # # if "apple" in fruit.values():
# # #     print(True)
# # # else:
# # #     print(False)
# #
# # # fruit.update({"weight": 200})
# # # fruit.update({"quantity": 120})
# # # fruit["price"] = 12_000_000
# #
# # # fruit.pop("name")
# #
# # # fruit.popitem()
# #
# # # del fruit["weight"]
# # # del fruit
# #
# # # print(fruit)
# #
# # # fruit = {
# # #     'name': "apple",
# # #     'color': "blue",
# # #     'weight': 100,
# # # }
# #
# # # apple = dict(fruit)
# # #
# # # apple['color'] = "red"
# # #
# # #
# # # print(apple, fruit, sep="\n")
# # #
# # #
# # # user = {
# # #     "location": {
# # #         "country": "Uzbekistan",
# # #         "city": ""
# # #     }
# # # }
# # #
# # # print(user["location"]["country"])
# #
# # # print(fruit.items())
# # # for key, value in fruit.items():
# # #     print(f"{key}: {value}")
# #
# # user = {
# #     "name": "Dilshod",
# #     "lastname": "Murtazoyev",
# #     "age": 25,
# #     "gender": "M",
# #     "job": "Engineer",
# #     "email": "dilshod@gmail.com",
# #     "phone": "+1 9876543210",
# #     "skills": ["python", "javascript", "HTML", "CSS", "ReactJS", "NodeJS", "NextJS"],
# #     "isMarred": True,
# # }
# #
# #
# # user.setdefault("age", 28)
# #
# # user["isMarred"] = False
# #
# # print("\n".join([f"{key}: {value}" for key, value in user.items()]))
# #
# #
# name = input("Add the name ::: ")
# addthenum = int(input("add the grade :: "))
# students = {
#     "Muhammad":100,
#     "Ahmad":80,
#     "Aysha":79,
#     "Abdyrahman":69
# }
# import time
# import sys
#
# def loading_prank():
#     print("Запуск системы... Пожалуйста, подождите.")
#     time.sleep(2)
#     for i in range(101):
#         sys.stdout.write(f"\rЗагрузка: {i}%")
#         sys.stdout.flush()
#         time.sleep(0.05)
#
#     print("\nОшибка! Система обнаружила следующее:")
#     time.sleep(2)
#     print("😱 Слишком много красоты на этом устройстве!")
#     time.sleep(1)
#     print("Решение найдено: отправь другу 'Ты супер!' ✨")
#     time.sleep(2)
#     print("Удачи! 😊")
#
# # Запускаем прикол
# loading_prank()
# Функция для создания словаря из имен и фамилий
def create_name_dictionary():
    people_count = int(input("Сколько людей вы хотите добавить? "))
    name_dict = {}

    for _ in range(people_count):
        first_name = input("Введите имя: ")
        last_name = input("Введите фамилию: ")
        name_dict[first_name] = last_name

    return name_dict


# Вызов функции и вывод результата
name_dictionary = create_name_dictionary()
print("\nПолученный словарь:")
print(name_dictionary)
