# numbers = input("add the numbers ::: ").split(" ")
# numbers = [int(i) for i in numbers]
# print(numbers)
# l = len(numbers)
# c = 0
# n = []
# for i in numbers:
#     c +=i
# middle = c // l
# print(middle)
# for i in numbers:
#     if middle < i:
#         n.append(i)
#     else:
#         pass
# print(n)
# # 2
# numbers = input("add the arr: ").split(" ")
# numbers = [int(i) for i in numbers]
#
# changed = True
# while changed:
#     changed = False
#     for i in range(1, len(numbers)):
#         if numbers[i] > numbers[i - 1]:
#             numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]
#             changed = True
#
# print("answer:", numbers)
# # 3
# numbers = input("add the numbers by ' ' :: ").split(" ")
# numbers = [int(i) for i in numbers]
# print(numbers)
# numbers = sorted(numbers)
# counts = 1
# counts_arr = []
# if len(numbers) <= 10:
#     for i in numbers:
#         if i == counts:
#             counts_arr.append(i)
#             counts += 1
#         else:
#             pass
#     counts = 0
#     for i in counts_arr:
#         counts += 1
#         print(f"{counts}:{numbers.count(i) * "*"}")
# else:
#     print("add only 10 numbers !!!!")
# # 4
# number = list(map(int , input("add the number").split(" ")))
# if len(number) <= 5:
#     number = sorted(number)
#     print(number[len(number)-1],number[len(number)-2])
# else:
#     print("errore add the right answer !!!!")
# # 5
# strs = input("add the string :: ")
# if len(strs) <= 7:
#     print(strs.count("cat"))
# else:
#     print("write onle 7 letters ")
# # 6
# name = list(input("add the name:: "))
# counts = 0
# while len(name) >= counts:
#     x = name[counts:] + name[:counts]
#     print("".join(x))
#     counts+=1
# # 7
# number = list(map(int , input("add the number after 3 put ' '").split(" ")))
# counts = 0
# counts_2 = 0
# for i in number:
#     counts_2 = number[counts]
#     counts_2 = [int(i) for i in counts_2]
#     print(counts_2)
#
# 7
# number = list(map(int , input("add the number after 3 put ' '").split(" ")))
# if len(number) != 9:
#     print("errore")
# else:
#     matrix = [number[:3],number[3:6],number[6:9]]
#     d = sum(matrix[i][i] for i in range(3))
#     print(d)
#
# number = list(map(int , input("add the number after 3 put ' '").split(" ")))
# if len(number) == 5:
#     for i in number:
#         if i == 1:
#             print("one")
#         elif i == 2:
#             print("two")
#         elif i == 3:
#             print("three")
#         elif i == 4:
#             print("four")
#         elif i == 5:
#             print("five")