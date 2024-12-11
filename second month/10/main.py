class User:
    name = ""
    surname = ""
    age = ""
    level_in_game = ""
    delORG = None
    def __del__(self, org):
        self.delORG = "sardor"
        if type(self.delORG) == str:
            del self.delORG
            return f"delOrg was delet {self.delORG}"
        return f"delOrg was not delet {self.delORG}"
    def __init__(self , name , surname , age , level ):
        self.name = name
        self.surname = surname
        self.age = age
        self.level_in_game = level

    def __str__(self):
        self.delORG = 123
        print(f"name: {self.age}")

user_1 = User("sardor","akobirov",16,15)

print(user_1.name)
user_2 = User("suxrob","akobirov",(1982 - 2024),55)
print(user_2.level_in_game)
print(user_2.__del__("sardor"))
# #
# #
# # class Student:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #         self.grades = []
# #
# #     def add_grade(self, grade):
# #         self.grades.append(grade)
# #
# #     def get_average_grade(self):
# #         if self.grades:
# #             return sum(self.grades) / len(self.grades)
# #         return 0
# #
# #     def __str__(self):
# #         return f"Имя: {self.name}, Возраст: {self.age}, Средний балл: {self.get_average_grade():.2f}"
# #
# #
# # student1 = Student("Алиса", 20)
# # student2 = Student("Боб", 22)
# #
# # student1.add_grade(85)
# # student1.add_grade(90)
# # student1.add_grade(78)
# #
# # student2.add_grade(92)
# # student2.add_grade(88)
# #
# # print(student1)
# # print(student2)
#
# def plusOne(digits: list[int]) -> list[int]:
#     digits = [str(i) for i in digits]
#     digits = "".join(digits)
#     digits = int(digits)
#     digits += 1
#     digits = str(digits)
#     onwer = list(digits)
#     onwer = [int(i) for i in onwer]
#     return onwer
# print(plusOne([1,2,3]))
#
#
# class Solution:
#     def plusOne(self, l: List[int]) -> List[int]:
#         s = ""
#         for i in l:
#             s += str(i)
#             k = int(s)
#         p = k + 1
#         l1 = []
#         for i in str(p):
#             l1.append(int(i))
#         return l1
#
