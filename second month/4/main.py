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

# 4
str = list(input("add the voise :: ").lower())
str = sorted(str)
print(str)








#
# n = list(map(int, input("Sonlarni vergul bilan ajratib kiriting: ").split(',')))
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
# print(f"Eng kichik ikkita elementning yig'indisi :: {(x + y)}")
# print(f"Nisbat :: {result:.2f}")
#
#7
# from itertools import permutations
#
# num = [1, 2, 3, 4, 5, 6]
#
# a = permutations(num, 3)
#
# x = 0
# for i in a:
#     if sum(i) == 10:
#         print(i)
#         x += 1
#
# print(f"Umumiy holatlar soni: {x}")


