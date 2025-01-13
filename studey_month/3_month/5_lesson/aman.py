# # import pandas
# # import requests
# # import json
# #
# #
# # a = requests.get("https://dummyjson.com/users").json()
# # for i in a["users"]:
# #     print(i["hair"])
# #
# # def change(arg: str, ver)-> list:
# #     verable = []
# #     for i in ver["users"]:
# #         a = i["hair"]
# #         verable.append(a.get("color", "black"),)
# #
# #     return verable
# #
# # print(change("hair",a))
# # # def change(arg: dict, strs: str) -> list:
# # #     arr = []
# # #     for i in arg:
# # #         x = arg.get(strs,"hello")
# # #         arr.append(x)
# # #     return arr
# # #
# # #
# # # print(change(a , "hair"))
# #
# # import random
# # import datetime
# #
# # # Список задач для развития в Python
# # tasks = [
# #     "Изучи новую концепцию Python (например, декораторы)",
# #     "Реши 3 задачи на LeetCode",
# #     "Создай маленький проект (например, калькулятор или заметки)",
# #     "Прочитай статью по программированию",
# #     "Посмотри обучающее видео и напиши конспект",
# #     "Участвуй в хакатоне или соревновании",
# #     "Перепиши старый проект с использованием новых знаний"
# # ]
# #
# # # Советы по дисциплине
# # tips = [
# #     "Установи четкие цели на неделю и следуй им",
# #     "Создай расписание и придерживайся его",
# #     "Разделяй большие задачи на маленькие и решай по одной",
# #     "Отключи отвлекающие факторы во время работы",
# #     "Отдыхай, но делай это с пользой (спорт, книги)",
# #     "Проводите 15 минут в день на повторение старого материала",
# #     "Записывай прогресс в дневник и анализируй его каждый месяц"
# # ]
# #
# # # Генерация случайной задачи и совета на день
# # def daily_task_and_tip():
# #     task = random.choice(tasks)
# #     tip = random.choice(tips)
# #     today = datetime.date.today().strftime("%d-%m-%Y")
# #     print(f"Сегодня ({today}):")
# #     print(f"\nЗадача: {task}")
# #     print(f"Совет: {tip}")
# #
# # if __name__ == "__main__":
# #     daily_task_and_tip()
# # ё
#
# class Sardor :
#     def __init__(self, name, surname ):
#         self.name = name
#         self.surname = surname
#     def __str__(self):
#         print(self.name , self.surname)
#
# user = Sardor("sardor","akobirov")
#
# print(user)





















