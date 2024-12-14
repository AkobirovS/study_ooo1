# # # # # from tkinter.font import names
# # # # #
# # # # #
# # # # # class User :
# # # # #     def __init__(self):
# # # # #         self.name = {}
# # # # #     def __getitem__(self, item):
# # # # #         return f"name is {self.name.get(item, "juk !!!")}"
# # # # #
# # # # #     def __setitem__(self, key, value):
# # # # #         if type(self.name[key]) == int:
# # # # #             self.name[key] = value * 2
# # # # #         else:
# # # # #             return "hello"
# # # # #         return self.name
# # # # #
# # # # #     def __delitem__(self, key):
# # # # #         if key in self.name:
# # # # #             print(f"{key} del buladi !!!")
# # # # #             del self.name[key]
# # # # #         else:
# # # # #             print("malumot yuk")
# # # # #
# # # # #     def __len__(self):
# # # # #         # if len(self.name) == 4:
# # # # #         #     return len(self.name)-1
# # # # #         # else:
# # # # #         #     return len(self.name)+1
# # # # #         return len(self.name)
# # # # # user1 = User()
# # # # # user1.name["name"] = "sardor"
# # # # # user1.name["name2"] = 2
# # # # # user1.name["name3"] = 2
# # # # # user1.name["name4"] = 2
# # # # # print(user1.name["name"].__len__())
# # # # # # print(user1.__setitem__("name",2))
# # # # # # print(user1.__delitem__("name1"))
# # # # # # print(user1.__delitem__("name1"))
# # # # # # print(user1["name2"])
# # # # #
# # # # #
# # # #
# # # #
# # # # class Cats:
# # # #     Name = ""
# # # #     Types = ""
# # # #     Age = None
# # # #     def __init__(self,name,types,age):
# # # #         self.Name = name
# # # #         self.Types = types
# # # #         self.Age = age
# # # #         self.kittens = {}
# # # #
# # # #     def __call__(self, *args, **kwargs):
# # # #         overEl = {}
# # # #         for i in range(len(args)):
# # # #             overEl[i] = args[i]
# # # #             print(f"pleace use these {overEl.items()} and in Init !!!")
# # # #         return "!!!!  pleace  !!!!!"
# # # #
# # # #     def __repr__(self):
# # # #         return "maybe this have one anothe avanue for kittens"
# # # #
# # # #     def __str__(self):
# # # #         return f"Hi this shop for get Cats an\nfirst by first add your cat information\nif your cat have kitten use the __setitem__\nif do you want to know , do suit you kitten us use __getitem__\nuse the __len__ for get you money"
# # # #
# # # #     def __del__(self):
# # # #         print("we get onle 10 or younger years old cats !!")
# # # #         if self.Age > 10:
# # # #             print(f"this cat does not suit us {self.Name}")
# # # #             del self.Name
# # # #             del self.Age
# # # #             del self.Types
# # # #             return "excusme for it !!"
# # # #         else:
# # # #             return "you cat suit us"
# # # #
# # # #     def __setitem__(self, key, value):
# # # #         self.kittens[key] = value
# # # #
# # # #     def __getitem__(self, item):
# # # #         if self.kittens[item] > 5:
# # # #             return "we are so sorry but\nyour kittens do not suit us"
# # # #         else:
# # # #             return "you kittens suit us"
# # # #
# # # #     def __delitem__(self, key):
# # # #         onswer = input("does not you want to give your kitten ? use y or n ::: ")
# # # #         if onswer == "n":
# # # #             del self.kittens[key]
# # # #             return "we delet this kitten"
# # # #         else:
# # # #             return "ok it is good for us thank you !!!"
# # # #
# # # #     def __len__(self):
# # # #         lens = len(self.kittens)
# # # #         return f"we give you for kittens {lens}00$ and for your cat 100$"
# # # #
# # # # cat1 = Cats("Alfa","zamurskie",7)
# # # # cat1.__setitem__("Alfamini",5)
# # # # cat1.__setitem__("sashka",2)
# # # # cat1.__setitem__("rijik",3)
# # # # # print(cat1.__getitem__("sashka"))
# # # # # print(cat1.__del__())
# # # # # print(len(cat1.kittens))
# # # # # print(cat1)
# # # # # print(cat1.__delitem__("sashka"))
# # # # print(cat1.__len__())
# # #
# # # class Numbers:
# # #     Number = None
# # #     def __init__(self , number):
# # #         self.Number = number
# # #
# # #     def __eq__(self, other):
# # #         return self.Number == other
# # #
# # #     def __lt__(self, other):
# # #         return self.Number < other
# # #
# # #     # def __gt__(self, other):
# # #     #     return self.Number > other
# # # n1 = Numbers(10)
# # # n2 = Numbers(11)
# # # print(n1 == n2)
# # # print(n2 < n1)
# # # import platform
# # # import os
# # # print(platform.system())
# # # print(dir(platform))
# # # print()
# # # os.remove()
# #
# #
# # def singleNumber(self, nums: list[int]) -> int:
# #     nums = sorted(nums)
# #     for i in nums:
# #         over_answer = nums[i:]
# #         if i in over_answer:
# #             return i
# #         else:
# #             pass
# #
#
# def singleNumber(self, nums: List[int]) -> int:
#     for i in nums:
#         if nums.count(i) == 1:
#             return i
#         else:
#             pass
class Task:
    def __init__(self, description, status="Не выполнена"):
        self.description = description
        self.status = status

    def mark_as_done(self):
        self.status = "Выполнена"

    def __str__(self):
        return f"{self.description} - {self.status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"Задача добавлена: '{description}'")

    def list_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def complete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1].mark_as_done()
            print(f"Задача '{self.tasks[task_number - 1].description}' выполнена!")
        else:
            print("Некорректный номер задачи.")

    def remove_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Задача '{removed_task.description}' удалена.")
        else:
            print("Некорректный номер задачи.")


# Пример использования
if __name__ == "__main__":
    manager = TaskManager()

    while True:
        print("\n1. Добавить задачу")
        print("2. Показать задачи")
        print("3. Отметить задачу как выполненную")
        print("4. Удалить задачу")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            description = input("Введите описание задачи: ")
            manager.add_task(description)
        elif choice == "2":
            manager.list_tasks()
        elif choice == "3":
            manager.list_tasks()
            task_number = int(input("Введите номер задачи для выполнения: "))
            manager.complete_task(task_number)
        elif choice == "4":
            manager.list_tasks()
            task_number = int(input("Введите номер задачи для удаления: "))
            manager.remove_task(task_number)
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")
