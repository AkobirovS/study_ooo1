# # 1# number = int(input("add the number :: "))
# # counts = 1
# # ls = []
# # while counts <= number:
# #     o = number % 2
# #     o_2 = number // 2
# #     number = o_2
# #     ls.append(o)
# #
# # print(ls[::-1])
# # 2
# # splits = [1, 2, 5, 2, 5, 4, 4, 5]
# # counts = 0
# # while counts < len(splits):
# #     counts_2 = counts + 1
# #     while counts_2 < len(splits):
# #         if splits[counts] == splits[counts_2]:
# #             del splits[counts_2]
# #         else:
# #             counts_2 += 1
# #     counts += 1
# #
# # print(splits)
# # 3
# # word_1 = input("add the word ")
# # word_2 = input("add the word_2 ")
# # arr = [sorted(word_1),sorted(word_2)]
# # if len(word_1) == len(word_2) and arr[0] == arr[1]:
# #     print("Анаграмма")
# # else:
# #     print("не Анаграмма ")
# # # 4
# # number = int(input("add the number_1 :: "))
# # number_2 = int(input("add the number_2 :: "))
# # simble = input("add the simble :: ")
# # if simble == "*":
# #     print(number * number_2)
# # elif simble == "/":
# #     print(number / number_2)
# # elif simble == "+":
# #     print(number + number_2)
# # elif simble == "-":
# #     print(number - number_2)
# # else:
# #     print("place use only + / * -")
#
# # 5
# number = int(input("add the number ::"))
# counts = 0
# counts_2 = 1
# counts_3 = 1
# while number > counts:
# print(counts_3)
# 5
# def fibonacci(n):
#     # Базовый случай: если n равно 0, то возвращаем 0
#     if n == 0:
#         return 0
#     # Базовый случай: если n равно 1, то возвращаем 1
#     elif n == 1:
#         return 1
#     # Рекурсивный случай: возвращаем сумму двух предыдущих чисел
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
# # 6
# numbers = int(input("add the number:: "))
# arr = []
# for i in range(3,numbers):
#     if i % 1 == 0 and i%i == 0:
#         arr.append(i)
#     else:
#         pass
# print(arr)
# 1
# numbers = input("add the numbers")
# arr = numbers.split(" ")
# s = int(arr[1])
# l = 0
# # for i in range(len(numbers)):
# #     l += i
# print(arr)
# print(type(arr[0]))
# print(int(arr[0]))
# print(type(arr[0]))lamda