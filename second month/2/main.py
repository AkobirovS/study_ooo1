# # 1
# numbers = int(input("add the numbers :: "))
# arr = []
# if 1 < numbers < 10:
#     for i in range(1, numbers + 1):
#         if i % 2 == 0:
#             pass
#         else:
#             arr.append(i)
# else:
#     pass
# print(arr)
# 2
# numbers = int(input("add the numbers :: "))
# arr = []
# if 1 < numbers < 10 :
#     for i in range(1,numbers+1):
#         i = 2 ** i
#         arr.append(i)
# else:
#     print("add the over 10 numer :: ")
# print(arr)
# # 3
# numbers = int(input("add the numbers n :: "))
# a = int(input("add the numbers a :: "))
# b = int(input("add the numbers d :: "))
# arr = []
# if 10 >= numbers and a and b > 0:
#     for i in range(1,numbers + 1):
#         a = a + b
#         arr.append(a)
# else:
#     print("add nuber over 10")
# print(arr)
# # 4
# numbers = int(input("add the numbers :: "))
# a = int(input("add the numbers a :: "))
# d = int(input("add the numbers d :: "))
# arr = []
# if 10 >= numbers > 1:
#     for i in range(1,numbers+1):
#         a = a * d
#         arr.append(a)
# else:
#     print("add the numbers over 10 please ")
# print(arr)
# 5
# n = int(input("add the numbers ::"))
# f_1 ,f_2 = 1 ,1
# for i in range(n):
#     print(f_1, end=" ")
#     f_1 , f_2 = f_2 ,f_2 +f_1
# 6
# numbers = int(input("add the number :: "))
# a = int(input("add the a number :: "))
# b = int(input("add the b number :: "))
# a_2 = []
# b = a + b
# if 2 <  numbers <= 10:
#     for i in range(2 , numbers + 1):
#         b += i
#         a_2.append(b)
# else:
#     print("use only over 10 !!")
# print(a_2)
# 7
# numbers = input("add the number n :: ")
# print(numbers[::-1])
# 8

# arr = [4,5,7,8,6,9]
# arr_2 = []
# n_1 = 0
# for i in arr:
#     n = arr.index(i)
#     if arr[n] % 2 != 0:
#         arr_2.append(arr[n])
#         n_1 +=1
#     else:
#         pass
# print(f"{arr_2} toglar soni {n_1}")

# 9
# arr = [4,5,7,8,6,9]
# arr_2 = []
# n_1 = 0
# for i in arr:
#     n = arr.index(i)
#     if arr[n] % 2 == 0:
#         arr_2.append(arr[n])
#         n_1 +=1
#     else:
#         pass
# print(f"{arr_2} toglar soni {n_1}")
# # 10
# arr = [4,5,7,8,6,9]
# arr_2 = []
# n_1 = []
# for i in arr:
#     n = arr.index(i)
#     if arr[n] % 2 == 0:
#         arr_2.append(arr[n])
#         arr_2 = sorted(arr_2)
#     else:
#         n_1.append(arr[n])
#         n_1 = sorted(n_1)
#         n_1 = n_1[::-1]
# print(f"{arr_2}{n_1}")

# # 18
# numbers = int(input("add the numbers :: "))
# numbers = list(range(1,numbers+1))
# print(numbers[0])
# # 19
# 20
# numbers = int(input("add the number :; "))
# k = int(input("add the number k  :; "))
# l = int(input("add the number l :; "))
# arr = list(range(numbers))
# numbers_2 = 0
# if 0 <= k <= l <= numbers:
#     k = arr.index(k)
#     l = arr.index(l)
#     arr = arr[k:l]
#     for i in arr:
#         numbers_2+=i
# else:
#     pass
# print(numbers_2)
# # 21
# nummber_1 = int(input("add the numbers :: "))
# k = int(input("add the numbers k :: "))
# l = int(input("add the numbers l :: "))
# if 0 <= k <= l <= nummber_1:
#     arr = list(range(k-1,l-1))
#     nummber_1 = 0
#     for i in arr:
#         nummber_1 += i
#     nummber_1 = nummber_1 // (l-k)
# else:
#     pass
# print(nummber_1)

# # 23
# numbers = int(input("add the numbers :: "))
# numbers_1 = 0
# k = int(input("add the numbers k :: "))
# l = int(input("add the numbers l :: "))
# arr = list(range(1,numbers+1))
# total_sum = sum(arr[:k]) + sum(arr[l:])
# print(total_sum)

# 23
# 00000 "I cant "
# numbers = int(input("add the numbers :: "))
# numbers_1 = 0
# k = int(input("add the numbers k :: "))
# l = int(input("add the numbers l :: "))
# arr = list(range(1,numbers+1))
# arr_2 = []
# arr_3 = list(range(1,k))
# arr_4 = list(range(l+1,numbers))
# arr_2.append(arr_3)
# arr_2.append(arr_4)
# print(arr_2)

# # 24
# number = [2,5,8,11,14]
# counts = 0
# counts_2 = 0
# arr = []
# while len(number)-1 > counts:
#     if len(number) != counts:
#         counts_2 = number[counts] - number[counts+1]
#     else:
#         pass
#     arr.append(counts_2)
#     counts += 1
# if arr[0] == arr[1]:
#     print(abs(arr[0]))
# else:
#     print(0)
#
# 25
# number = [2,5,8,11,14]
# counts = 0
# counts_2 = 0
# arr = []
# while len(number)-1 > counts:
#     if len(number) != counts:
#         counts_2 = number[counts] - number[counts+1]
#     else:
#         pass
#     arr.append(counts_2)
#     counts += 1
# if arr[0] == arr[1]:
#     print(abs(arr[0]))
# else:
#     print(0)
# #25
# number = [2,4,8]
# counts = 0
# counts_2 = 0
# arr = []
# while len(number)-1 > counts:
#     if len(number) != counts:
#         counts_2 = number[counts+1] / number[counts]
#     else:
#         pass
#     arr.append(counts_2)
#     counts += 1
# if arr[0] == arr[1]:
#     print(abs(arr[0]))
# else:
#     print(0)
#
# # 26 ??? cant did
# arr = [2,3,4,5,6,7]
# arr_2 = []
# counts_1 = 0
# counts_2 = []
# lens = len(counts_2)
#
# while len(arr) > counts_1:
#     if arr[counts_1] % 2 == 0:
#         counts_2.append(1)
#         while lens > counts_1:
#             if counts_2[counts_1] == 2:
#
#     elif arr[counts_1] % 2 != 0:
#         counts_2.append(2)
# # if arr == arr_2 :
# #     print("tgri")
# # else:
# # #     print("not")
# arr = [2,3,4,5,6,7]
# lens = len(arr)
# counts = 0
# while lens > counts:
#     if arr[counts] % 2 == 0 and arr[lens-2] % 2 == 0:
#         print("tigri")
#     elif arr[counts] % 2 != 0 and arr[lens-2] % 2 != 0:
#         print("tigri")
#     else:
#         print(0)
#     counts += 2