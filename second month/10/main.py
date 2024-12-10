# # class User:
# #     name = None
# #     surname = None
# #     age = None
# #     level_in_game = None
# #
# #     def __init__(self , name , surname , age , level ):
# #         name = self.name
# #         surname = self.surname
# #         age = self.age
# #         level = self.level_in_game
# #
# #
# # user_1 = User("sardor","akobirov",16,15)
# #
# # print(user_1)
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
