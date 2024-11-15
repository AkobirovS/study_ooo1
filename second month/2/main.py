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

# 19