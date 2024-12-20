# home
# first
# answer = input("add the archi something:: ")
# print(ord(answer))
# second
# answer = input("add some number:: ")
# if answer.isnumeric():
#     answer = int(answer)
#     print(chr(answer))
# else:
#     print(f"errore ::{answer}")
# third
# amswer = int(input("add number:: "))
# amswer += 1
# a = chr(amswer)
# amswer -= 2
# b = chr(amswer)
# print(a,b, sep="\n")
# forth
# answer = int(input("add new chr code:: "))
# if answer >= 1 & answer <=26:
#     print(chr(answer).upper())
# else:
#     print(f"errore: {answer}")
# fifth
# answer = int(input("hello:: "))
# if answer >= 1 & answer <= 26:
#     alfabit = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
#     alfabit = alfabit.lower().split(" ")
#     print(alfabit[::-1])
#     print(list(reversed(alfabit)))
# else:
#     print(f"error::{answer}")
# sixth
# answer = input("hello:: ")
# if answer.isnumeric():
#     print("digit")
# else:
#     print("lotin")
# seventh
# answer = input("add string:: ")
# answer = list(answer)
# print(answer[0],answer[-1],sep="\n")
# eight
# answer = int(input("add number:: "))
# answer_1 = input("pess a word:: ")
# print(answer * answer_1)
# naneth
# strs_1 = "hello"
# strs_2 = "world"
# print(strs_1 + " " + strs_2)
# tenth
# ten = "sardor"
# print(list(reversed(ten)))
# eleventh
from idlelib.replace import replace
from itertools import count
from operator import index

# 11
# s = input(":: ")
# count  = " ".join(s)
# print(count)
# 12?
# 27
# string_1 = "sardor"
# string_2 = "sardor"
# number_1 = 5
# number_2 = 5
# print(string_1[:number_1], string_2[-number_2:],sep="")
# 28
# srting = input("add somthing:: ")
# somethig = input("add something:: ")
#
# for i in srting:
#     if somethig == i:
#         print(srting.replace(i,somethig+i))
#     else:
#         pass
# 29
# s_1 = input("add str:: ")
# s_2 = input("add str:: ")
# c = input("add c:: ")
# if s_1.count(c) == True:
#     print(s_1.replace(c,s_2+c))
# else:
#     print("hello")
# 30
# s_1 = input("add str:: ")
# s_2 = input("add str:: ")
# c = input("add c:: ")
# if s_1.count(c) == True:
#     print(s_1.replace(c,c+s_2))
# else:
#     print("hello")
# 31
# s_1 = input("add somthig ")
# s_2 = input("add somthig ")
# print(s_2 in s_1)
# 32
# s_1 = input("add somthig ")
# s_2 = input("add somthig ")
# print(s_1.count(s_2))
# 33
# s_1 = input("add somthig ")
# s_2 = input("add somthig ")
# indexs = list(s_1)
#
# if s_2 in indexs:
#     del indexs[indexs.index(s_2)]
#     print("".join(indexs))
# else:
#     print(s_1)
# 34
# s_1 = input("add somthig ")
# s_2 = input("add somthig ")
# indexs = list(s_1)
# indexs = indexs[::-1]
#
# if s_2 in indexs:
#     del indexs[indexs.index(s_2)]
#     indexs = indexs[::-1]
#     print("".join(indexs))
# else:
#     print(s_1)
# 35
# s_1 = input("add somthig ")
# s_2 = input("add somthig ")
#
# print(s_1.replace(s_2,""))
# 36
# s_1 = input("add somethig ")
# s_2 = input("add somethig ")
# s_3 = input("add somethig ")
# if s_2 in s_1:
#     x = s_1.replace(s_2,s_2 + s_3)
#     print(x)
# else:
#     pass
# 37
# s_1 = input("add somethig ")
# s_2 = input("add somethig ")
# s_3 = input("add somethig ")
# s_1 = s_1[::-1]
# if s_2 in s_1:
#     x = s_1.replace(s_2, s_3,1)
#     x = x[::-1]
#     print(x)
# else:
#     pass