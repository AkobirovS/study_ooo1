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
# 2
# numbers = input("add the numbers by ' ' speac  " ).split(" ")
# numbers = [int(i) for i in numbers]
# l = len(numbers)
# counts = 0
# while len(numbers) > counts:
#     if numbers[counts] > numbers[l-(len(numbers)-1)]:
#         numbers[counts] = numbers[l-(len(numbers)-1)]
#     else:
#         numbers[counts] = numbers[l-(len(numbers)-1)]
#     counts+=1
#     l -=1
# print(numbers)
# 6
# name = list(input("add the name:: "))
# counts = 0
# while len(name) >= counts:
#     x = name[counts:] + name[:counts]
#     print("".join(x))
#     counts+=1