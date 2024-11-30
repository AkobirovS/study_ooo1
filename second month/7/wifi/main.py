## # def twoSum(nums, target):
# # #     lists = []
# # #     counts = 0
# # #     for i in range(0, len(nums) - 1):
# # #         x = nums[counts] + nums[counts +1]
# # #         counts +=1
# # #         print(x)
# # #         if x == target:
# # #             lists.append(nums.index(counts))
# # #             lists.append(nums.index(counts))
# # #             return [nums.index(counts) , nums.index(counts+1)]
# # # print(twoSum([1,2,3,4,5],7))
# # #
# # #
# # # def isPalindrome(x: int) -> bool:
# # #     x = str(x)
# # #     strs = reversed(x)
# # #     strs = "".join(strs)
# # #     if x == strs:
# # #         return True
# # #     else:
# # #         return False
# # #
# # #
# # # print(isPalindrome(123))
# s = str(input("Add the rim numbers:: "))
# # def ramanToInt(s: str):
# #     s = s.lower()
# #     s = list(s)
# #     l = ["i","v","x","l","c","d","m"]
# #     c = 0
# #     for i in s:
# #         print(c)
# #         if i == "i":
# #             c += 1
# #         elif i == "v":
# #             c+=5
# #         elif i == "x":
# #             c+=10
# #         elif i == "l":
# #             c+=50
# #         elif i == "c":
# #             c+=100
# #         elif i == "d":
# #             c+=500
# #         elif i == "m":
# #             c+=1000
# #         else:
# #             return "errore"
# #     return c
# # print(ramanToInt(strs))
# def romanToInt(s: str):
#     s = s.lower()
#     roman_map = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}
#     total = 0
#     prev_value = 0
#     for char in reversed(s):
#         value = roman_map.get(char, 0)
#         total += value
#         print(total)
#     for i in s:
#         v = roman_map.values()
#
# romanToInt(s)
# strs = ["dog","racecar","car"]
# if len(strs) != 0:
#     strs_3 = strs[0]
#     for i in strs[1:]:
#         if i.startswith(strs_3):
#             print(strs_3)
#                 # return strs_3
#         else:
#             strs_3 = strs_3[:-1]
#             print(strs_3)
#             print(strs)
# else:
#     print("hhell")
