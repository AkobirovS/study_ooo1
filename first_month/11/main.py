# -1
# string_1 = input("add the word:: ")
# if string_1.isnumeric():
#     print(f"add the word pleace dont add the number {string_1}")
# else:
#     if string_1.isupper():
#         s = string_1.lower()
#         print(s)
#     else:
#         s = string_1.upper()
#         print(s)

# 1
# letters = input("add the letter:: ")
# if letters.isnumeric():
#     print("none")
# else:
#     if letters.isupper():
#         print(letters.lower())
#     else:
#         print(letters.upper())
# 2
# a = int(input("hello: add number:: "))
# b = int(input("hello add second number:: "))
# if a == b :
#     print(a + b)
# else:
#     print(a + b, "o" in "uzzbekistan")
# 3
# a = 5
# b = 4
# if a != b:
#     if a < b:
#         print(b)
#     else:
#         print(a)
# else:
#     print(a + b)
# 4
# a = 10
# b = 8
# c = 10
# if a > b and a > c:
#     print(a)
# elif b > a and b > c and:
#     print(b)
# else:
#     print(c)
# or
# l = [a,b,c]
# print(l[1])
# a = int(input(":: "))
# b = int(input(":: "))
# c = int(input(":: "))
# n = sorted([a,b,c])
# print(n[0],n[1],n[2], sep="")
# 4
# a = int(input("number:: "))
# v = int(input("number::"))
# b = int(input("nuber:: "))
# n = sorted([a,v,b])
# print(n[0],n[1])
# 5
# a = int(input("number:: "))
# v = int(input("number::"))
# b = int(input("nuber:: ")) + v
# import math
#
# gcd = math.gcd(a, b)
#
# lcm = (a * b) // gcd
#
# # Выводим результат
# print("Наибольший общий делитель (НОД):", gcd)
# print("Наименьшее общее кратное (НОК):", lcm)
#
# 6
# a = int(input("number:: "))
# b = int(input("number:: "))
# c = int(input("number:: "))
# n = sorted([a,b,c])
# n_2 = [a,b,c]
# if n == n_2:
#     print("222")
# else:
#     print(a+b+c)
# 7
#
# a = int(input("number:: "))
# b = int(input("number:: "))
# c = int(input("number:: "))
# l = [a, b, c]
# k = sorted(l)
# counts = 0
# while counts < 1:
#     counts+=1
#     if l == k[::-1]:
#         print(a + b + c)
#     elif b == c:
#         print(a + b + c)
#     elif a == b or a == c or b == a:
#         print(a + b + c)
#     else:
#         print(print(222))
# 8
#
#
# a = int(input("number:: "))
# b = int(input("number:: "))
# c = int(input("number:: "))
# l = sorted([a,b,c])
# n = []
# for i in l:
#     n = l.count(i)
#     if n == 2:
#         x = l.index(i)
#         print(x)
#     else:
#         pass
# 9
#
# a = int(input("hello:: "))
# a_1 = int(input("hello:: "))
# a_2 = int(input("hello:: "))
# a_3= int(input("hello:: "))
# if a == a_1 == a_2:
#     print(a_3)
# elif a == a_1 == a_3:
#     print(a_2)
# elif a == a_2 == a_3:
#     print(a_1)
# else:
#     print(a)
# # Вводим координаты точек A, B и C
# a = float(input("Введите координату точки A: "))
# b = float(input("Введите координату точки B: "))
# c = float(input("Введите координату точки C: "))
#
# a_b = (a-b)
# a_c = (a-c)
# if a_b > a_c:
#     print(f"b yakinroq {a_b}")
# else:
#     print(f"a yakinroq {a_c}")