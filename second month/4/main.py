# # 1
# arr = input("add the number by ' ': ")
# by = [int(arr) for arr in arr.split()]
# answer = []
# for i in range(len(by)):
#     sums = 0
#     for j in range(len(by)):
#         if i != j:
#             sums += by[j]
#     answer.append(sums)
#
# print(f"answer :: {answer}")


# # 2
# strs_1 = input("add the string:: ")
# strs_2 = input("add the second string:: ")
# for i in strs_1:
#     if i == "a":
#         strs_1 = strs_1.replace(i,strs_2)
#     elif i == "e":
#         strs_1 = strs_1.replace(i,strs_2)
#     elif i == "i":
#         strs_1 = strs_1.replace(i,strs_2)
#     elif i == "o":
#         strs_1 = strs_1.replace(i,strs_2)
#     elif i == "i":
#         strs_1 = strs_1.replace(i,strs_2)
#     else:
#         pass
# print(strs_1)
# 3
# arr = list(input("add str list :: "))
# arr_2 = []
# strs = list(input("add str :: "))
# l = len(strs)
# print(arr[l:])
#
# # 4
# str = list(input("add the voise :: ").lower())
# l = []
# str = sorted(str)
# counts = 0
# while len(str) > counts:
#     x = str.count(str[counts])
#     l.append(x)
#     counts+=1
# counts_1 = 0
# while len(str) > counts_1:
#     if max(l) == str.count(str[counts_1]):
#         print(str[counts_1])
#         break
#     else:
#         pass
#     counts_1+=1
# 5
# arr = ["sardor","alixon","faruh"]
# str = ""
# for i in arr:
#     str += f"hello {i} "
# print(str)
#6
# n = list(map(int, input("add the numbers by ',': ").split(',')))
#
# a = float('-inf')
# b = float('-inf')
#
# for i in n:
#     if i > a:
#         b = a
#         a = i
#     elif i > b:
#         b = i
#
# x, y = float('inf'), float('inf')
# for i in n:
#     if i < x:
#         y = x
#         x = i
#     elif i < y:
#         y = i
#
# result = (a + b) / (x + y)
#
# print(f"the big number :: {(a + b)}")
# print(f"the smoller 2 number :: {(x + y)}")
# print(f"answer :: {result:.2f}")
#
# 7
# num = list(map(int,input("add the numbers")))
#
# x = 0
#
# for i in range(len(num)):
#     for j in range(i + 1, len(num)):
#         for k in range(j + 1, len(num)):
#             if num[i] + num[j] + num[k] == 10:
#                 print((num[i], num[j], num[k]))
#                 x += 1
#
# print(f"tens: {x}")
#











# # 50
# import random
# from operator import ifloordiv
#
# number = int(input("add the number len ::: "))
# arr = []
# for i in range(1,number+1):
#     x = random.randint(1,9)
#     arr.append(x)
# arr_2 = []
# for i in range(1,number+1):
#     x = random.randint(1,9)
#     arr_2.append(x)
# print(arr,arr_2)
# f = arr.copy()
# x = arr_2.copy()
# del arr[:]
# del arr_2[:]
# arr_2.append(f)
# arr.append(x)
# print(arr,arr_2)
# 52
# import random
# number = int(input("add the numbers :: "))
# arr = []
# for i in range(1,number+1):
#     x = random.randint(1,9)
#     arr.append(x)
# arr_2 = []
# for i in range(1,number+1):
#     x = random.randint(1,9)
#     arr_2.append(x)
# print(arr,arr_2)
# counts = 0
# while counts < number:
#     if arr[counts] < 5:
#         arr_2[counts] = 2*arr[counts]
#     else:
#         arr_2[counts] = arr[counts]/2
#     counts+=1
# print(arr_2)
# 53
# import random
# numbers = int(input("add the number for len :: "))
# a = []
# b = []
# c = []
# for i in range(numbers):
#     a.append(random.randint(1,9))
#     b.append(random.randint(1,9))
# print(a,b)
# counts = 0
# while numbers > counts:
#     c.append(max(a[counts],b[counts]))
#     counts +=1
# print(c)
# 54
# import random
# numbers = int(input("add the numbers for len :: "))
# a = []
# b = []
# for i in range(numbers):
#     a.append(random.randint(1,9))
# counts = 0
# while counts < numbers:
#     while counts % 2 == 0:
#         b.append(a[counts])
#         break
#     counts += 1
# print(a,b,sep="\n")
# none
# 55
# import random
# numbers = int(input("add the numbers for len :: "))
# a = []
# b = []
# for i in range(numbers):
#     a.append(random.randint(1,9))
# counts = 0
# while counts < numbers:
#     while counts % 2 != 0:
#         b.append(a[counts])
#         break
#     counts += 1
# print(a,b,sep="\n")
# # 56
# import random
# numbers = int(input("add the numbers for len :: "))
# a = []
# b = []
# for i in range(numbers):
#     a.append(random.randint(1,9))
# counts = 0
# while counts < numbers:
#     counts += 1
#     while counts % 3 == 0:
#         b.append(a[counts])
#         break
# print(a,b,sep="\n")
