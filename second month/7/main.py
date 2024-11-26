# 1
# lesn = int(input("how many county you wont add ? :: "))
# dicts = {}
# for i in range(lesn):
#     name = input("add the name of country ::  ")
#     stats = input("add the name of capital :: ")
#     dicts[i] = dict(name=f"{stats}")
#
# print(dicts.items())
#2
# lesn = int(input("how many county you wont add ? :: "))
# dicts = {
#     "uzb":"tash",
#     "rus":"mos"
# }
# for i in range(lesn):
#     name = input("add the name of country ::  ")
#     stats = input("add the name of capital :: ")
#     dicts[name] = stats
# for key , velue in dicts.items():
#     print(key+"  "+velue)
#
# print(dicts.items())
# 3
# dicts = {
#     "uzb":"tash"
# }
# print(dicts.items())
# # dicts["uzb"] = "sam"
# # print(dicts.items())
# # 4
# # dicts = {
# #     "uzb":"tash",
# #     "rus":"mos"
# # }
# # print(dicts.items())
# # dicts.pop("uzb")
# # print(dicts.items())
#
#
#
# #
# import math
#
# a = int(input("add the numbers :: "))
# b = int(input("add the numbers :: "))
# c = int(input("add the numbers :: "))
# d = float(input("add the numbers float :: "))
# e = float(input("add the numbers float :: "))
#
#
# def powerA3(a):
#     print(a**3)
# powerA3(a)
# powerA3(b)
# powerA3(c)
# powerA3(d)
# powerA3(e)
import math


# 2
# a = float(input("add the numbers float :: "))
# d = float(input("add the numbers float :: "))
# c = float(input("add the numbers float :: "))
# def PowerA234(a):
#     print(a**2 ,a**3, a**4 ,sep="    ")
#
# PowerA234(a)
# PowerA234(d)
# PowerA234(c)

# 3
# a = float(input("add the numbers float :: "))
# b = float(input("add the numbers float :: "))
# c = float(input("add the numbers float :: "))
# d = float(input("add the numbers float :: "))
# def maen(a,b):
#     print((a + b) / 2 , math.sqrt(a*b) , sep="   ")
#
# maen(a,b)
# maen(a,c)
# maen(a,d)
#
# # 4
# soap = int(input("add the storana  a"))
# soap_2 = int(input("add the storana c "))
# soap_3 = int(input("add the storana b "))
# def taingle(a,b,c):
#     p = (a+c+b) / 2
#     s = math.sqrt(p * (p - a) * (p - b) * (p - c))
#     print(f"P = {a+b+c}  s = {s} ")
#
# taingle(soap,soap_2,soap_3)
# 5 ???
# 6
# num_1 = int(input("add the first number for 'a' :: "))
# num_2 = int(input("add the first number for 'b' :: "))
# num_3 = int(input("add the first number for 'c' :: "))

# def digit_counts_sum(a=int,b=int,c=int):
#     l = [a,b,c]
#     l = [str(i) for i in l]
#     s = 0
#     for i in l:
#         for _ in i:
#             _ = int(_)
#             s +=_
#     print(f"raqamlar summasi {s} sonlar sum {a+c+b}")
# digit_counts_sum(num_3,num_2,num_1)
# 7
# a = int(input("add the first number for 'a' :: "))
# b = int(input("add the first number for 'b' :: "))
# c = int(input("add the first number for 'c' :: "))
#
# def invert_digit(a,b,c):
#     s = sorted([a,b,c])
#     print(s)
#     print(s[::-1])
#
# invert_digit(a,b,c)
# # 8
# b = int(input("add the first number for 'r' :: "))
# c = int(input("add the first number for 'k' :: "))
# def add_right_digit(a,r):
#     if 0 < a < 9:
#         r = str(r)
#         a = str(a)
#         print(r+a)
#     else:
#         pass
# add_right_digit(c,b)
# 9

# b = int(input("add the first number for 'k' :: "))
# c = int(input("add the first number for 'r' :: "))
# def add_left_digit(a,r):
#     if 0 < r < 9:
#         r = str(r)
#         a = str(a)
#         print(a+r)
#     else:
#         pass
# add_left_digit(b,c)
# 10
def s_wap(a,b,c,d):
    ab = a+b
    cd = c+d
    print(ab,cd)
    cd,ab = ab,cd
    print(ab,cd)
s_wap(10,23,4,5)