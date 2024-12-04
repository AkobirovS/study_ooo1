# # # # # # # # # ## # def twoSum(nums, target):
# # # # # # # # # # # #     lists = []
# # # # # # # # # # # #     counts = 0
# # # # # # # # # # # #     for i in range(0, len(nums) - 1):
# # # # # # # # # # # #         x = nums[counts] + nums[counts +1]
# # # # # # # # # # # #         counts +=1
# # # # # # # # # # # #         print(x)
# # # # # # # # # # # #         if x == target:
# # # # # # # # # # # #             lists.append(nums.index(counts))
# # # # # # # # # # # #             lists.append(nums.index(counts))
# # # # # # # # # # # #             return [nums.index(counts) , nums.index(counts+1)]
# # # # # # # # # # # # print(twoSum([1,2,3,4,5],7))
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # # def isPalindrome(x: int) -> bool:
# # # # # # # # # # # #     x = str(x)
# # # # # # # # # # # #     strs = reversed(x)
# # # # # # # # # # # #     strs = "".join(strs)
# # # # # # # # # # # #     if x == strs:
# # # # # # # # # # # #         return True
# # # # # # # # # # # #     else:
# # # # # # # # # # # #         return False
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # # print(isPalindrome(123))
# # # # # # # # # # s = str(input("Add the rim numbers:: "))
# # # # # # # # # # # def ramanToInt(s: str):
# # # # # # # # # # #     s = s.lower()
# # # # # # # # # # #     s = list(s)
# # # # # # # # # # #     l = ["i","v","x","l","c","d","m"]
# # # # # # # # # # #     c = 0
# # # # # # # # # # #     for i in s:
# # # # # # # # # # #         print(c)
# # # # # # # # # # #         if i == "i":
# # # # # # # # # # #             c += 1
# # # # # # # # # # #         elif i == "v":
# # # # # # # # # # #             c+=5
# # # # # # # # # # #         elif i == "x":
# # # # # # # # # # #             c+=10
# # # # # # # # # # #         elif i == "l":
# # # # # # # # # # #             c+=50
# # # # # # # # # # #         elif i == "c":
# # # # # # # # # # #             c+=100
# # # # # # # # # # #         elif i == "d":
# # # # # # # # # # #             c+=500
# # # # # # # # # # #         elif i == "m":
# # # # # # # # # # #             c+=1000
# # # # # # # # # # #         else:
# # # # # # # # # # #             return "errore"
# # # # # # # # # # #     return c
# # # # # # # # # # # print(ramanToInt(strs))
# # # # # # # # # # def romanToInt(s: str):
# # # # # # # # # #     s = s.lower()
# # # # # # # # # #     roman_map = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}
# # # # # # # # # #     total = 0
# # # # # # # # # #     prev_value = 0
# # # # # # # # # #     for char in reversed(s):
# # # # # # # # # #         value = roman_map.get(char, 0)
# # # # # # # # # #         total += value
# # # # # # # # # #         print(total)
# # # # # # # # # #     for i in s:
# # # # # # # # # #         v = roman_map.values()
# # # # # # # # # #
# # # # # # # # # # romanToInt(s)
# # # # # # # # # # strs = ["dog","racecar","car"]
# # # # # # # # # # if len(strs) != 0:
# # # # # # # # # #     strs_3 = strs[0]
# # # # # # # # # #     for i in strs[1:]:
# # # # # # # # # #         if i.startswith(strs_3):
# # # # # # # # # #             print(strs_3)
# # # # # # # # # #                 # return strs_3
# # # # # # # # # #         else:
# # # # # # # # # #             strs_3 = strs_3[:-1]
# # # # # # # # # #             print(strs_3)
# # # # # # # # # #             print(strs)
# # # # # # # # # # else:
# # # # # # # # # #     print("hhell")
# # # # # # # # #
# # # # # # # # # # strs = ["dog","racecar","car"]
# # # # # # # # # # if len(strs) != 0:
# # # # # # # # # #     counts = 0
# # # # # # # # # #     main = strs[0]
# # # # # # # # # #     while counts < len(main):
# # # # # # # # # #         counts+=1
# # # # # # # # # #         if strs[counts].startswith(main):
# # # # # # # # # #             print(strs)
# # # # # # # # # #         else:
# # # # # # # # # #             main = main[:-1]
# # # # # # # # # #             counts -=1
# # # # # # # # # #             print(strs[counts])
# # # # # # # # # #             print(main)
# # # # # # # # # #     print()
# # # # # # # # # # else:
# # # # # # # # # #     print("errore")
# # # # # # # # # def longestCommonPrefix(strs):
# # # # # # # # #     if not strs:
# # # # # # # # #         return "error: there is nothing here !!"
# # # # # # # # #
# # # # # # # # #     prefix = strs[0]
# # # # # # # # #
# # # # # # # # #     for string in strs[1:]:
# # # # # # # # #         while not string.startswith(prefix):
# # # # # # # # #             prefix = prefix[:-1]
# # # # # # # # #             if not prefix:
# # # # # # # # #                 return ""
# # # # # # # # #
# # # # # # # # #     return prefix
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # print(longestCommonPrefix(["dog", "racecar", "car"]))
# # # # # # # # from math import log10
# # # # # # # #
# # # # # # # #
# # # # # # # # def addTwoNumbers(l, l_2):
# # # # # # # #     l = [str(l) for l in l]
# # # # # # # #     l_2 = [str(l) for l in l_2]
# # # # # # # #     if len(l) != 0 and len(l_2):
# # # # # # # #         print(l)
# # # # # # # #         l = l[::-1]
# # # # # # # #         l = "".join(l)
# # # # # # # #         l = int(l)
# # # # # # # #         l_2 = l_2[::-1]
# # # # # # # #         l_2 = "".join(l_2)
# # # # # # # #         l_2 = int(l_2)
# # # # # # # #         p = l_2 + l
# # # # # # # #         p = str(p)
# # # # # # # #         p = list(p)
# # # # # # # #         p = p[::-1]
# # # # # # # #         p = [int(i) for i in p]
# # # # # # # #         print(p)
# # # # # # # #     else:
# # # # # # # #         return "erore"
# # # # # # # # print(addTwoNumbers([2,4,3],[5,6,4]))
# # # # # # # # print(addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9]))
# # # # # # # #
# # # # # # # # def benaryCarch(number):
# # # # # # # #     left = 0
# # # # # # # #     rights = 100
# # # # # # # #
# # # # # # # #     while left < rights:
# # # # # # # #         mid = (rights + left) // 2
# # # # # # # #         answer = input(f"this is {mid} ")
# # # # # # # #         if answer == "y":
# # # # # # # #             return mid
# # # # # # # #         elif answer == "b":
# # # # # # # #             left = mid
# # # # # # # #             print(left)
# # # # # # # #         else:
# # # # # # # #             rights = mid
# # # # # # # #             print(rights)
# # # # # # # #
# # # # # # # #
# # # # # # # # print(benaryCarch(55))
# # # # # # # def isValid(s: str) -> bool:
# # # # # # #     lists = ["{}", "[]", "()"]
# # # # # # #     splits_s = list(s)
# # # # # # #     splits_s_l = []
# # # # # # #     splits_s_f = ""
# # # # # # #     if 1 <= len(s) <= (10 ** 4):
# # # # # # #         for i in range(1,4):
# # # # # # #             splits_s_f += splits_s[0]
# # # # # # #             splits_s_f += splits_s[len(splits_s) - 1]
# # # # # # #             splits_s_l.append(splits_s_f)
# # # # # # #             splits_s_f = ""
# # # # # # #             splits_s.remove(splits_s[0])
# # # # # # #             splits_s.remove(splits_s[len(splits_s) - 1])
# # # # # # #             if s == "()[]{}" or s == "{}[]()" or s == "(){}[]" :
# # # # # # #                 return True
# # # # # # #             if lists[0] == splits_s_l[0] or lists[0] == splits_s_l[len(splits_s)-1]:
# # # # # # #                 return True
# # # # # # #             elif lists[1] == splits_s_l[0] or lists[0] == splits_s_l[len(splits_s)-1]:
# # # # # # #                 return True
# # # # # # #             elif lists[2] == splits_s_l[0] or lists[0] == splits_s_l[len(splits_s)-1]:
# # # # # # #                 return True
# # # # # # #             else:
# # # # # # #                 return False
# # # # # # #     else:
# # # # # # #         return True
# # # # # # # print(isValid("()"))
# # # # # # # print(isValid("()[]{}"))
# # # # # # # print(isValid("(]"))
# # # # # # # print(isValid("([])"))
# # # # # #
# # # # # # def isValid(s: str) -> bool:
# # # # # #     if 0 < len(s) <= 10**4:
# # # # # #         if s == "()[]{}":
# # # # # #             return True
# # # # # #         else:
# # # # # #             string_list = []
# # # # # #             for i in range(len(s)):
# # # # # #                 f = s[0]
# # # # # #                 l = s[-1]
# # # # # #
# # # # # #
# # # # # #     else:
# # # # # #         return False
# # # # # from os import remove
# # # # #
# # # # #
# # # # # #
# # # # # # def isValid(s):
# # # # # #     if s == "()[]{}":
# # # # # #         return True
# # # # # #     elif 10 > len(s) > 0:
# # # # # #         answer = bool
# # # # # #         list_answers = ["{}","()","[]"]
# # # # # #         list_over = []
# # # # # #         copy_s = list(s)
# # # # # #         for i in range(len(s) // 2):
# # # # # #             last = copy_s[-1]
# # # # # #             firts = copy_s[0]
# # # # # #             copy_s.remove(copy_s[0])
# # # # # #             copy_s.remove(copy_s[-1])
# # # # # #             list_over.append(firts + last)
# # # # # #         for i in range(len(list_over)):
# # # # # #             if list_over[i] == list_answers[i] or list_over[i] == list_answers[i+1] or list_over[i] == list_answers[i+2]:
# # # # # #                 return True
# # # # # #     else:
# # # # # #         return None
# # # # # # print(isValid("({})"))
# # # # # # print(isValid("{[]}"))
# # # # # # print(isValid("()[]{}"))
# # # # # # print(isValid("(]"))
# # # # # # print(isValid("({})"))
# # # # # def isValid(self, s: str) -> bool:
# # # # #     if s == "()[]{}":
# # # # #         return True
# # # # #     elif 10 > len(s) > 1:
# # # # #         if len(s) % 2 == 0:
# # # # #             answer_t = 0
# # # # #             answer_f = 0
# # # # #             list_answers = ["{}", "()", "[]"]
# # # # #             list_over = []
# # # # #             copy_s = list(s)
# # # # #             for i in range(len(s) // 2):
# # # # #                 last = copy_s[-1]
# # # # #                 firts = copy_s[0]
# # # # #                 copy_s.remove(copy_s[0])
# # # # #                 copy_s.remove(copy_s[-1])
# # # # #                 list_over.append(firts + last)
# # # # #             counts = 0
# # # # #             while counts < len(s) // 2:
# # # # #                 if list_over[counts] in list_answers:
# # # # #                     answer_t += 1
# # # # #                 else:
# # # # #                     answer_f += 1
# # # # #                 counts += 1
# # # # #             if answer_t > answer_f:
# # # # #                 return True
# # # # #             else:
# # # # #                 return False
# # # # #         else:
# # # # #             return False
# # # # #     else:
# # # # #         return False
# # # # #
# # # # # print(isValid("({})"))
# # # # # print(isValid("{[]}"))
# # # # # print(isValid("()[]{}"))
# # # # # print(isValid("(]"))
# # # # # print(isValid("({})"))
# # # # # print(isValid("({[)"))
# # # #
# # # #
# # # # def jump(nums):
# # # #     bools = True
# # # #     counts_2 = 0
# # # #     while bools:
# # # #         counts_2+=1
# # # #         over_el = nums[0]
# # # #         do = nums[1:over_el+1]
# # # #
# # # #         counts = 0
# # # #         while counts < len(do):
# # # #             if do[counts] > do[-1]:
# # # #                 do.remove(do[-1])
# # # #             else:
# # # #                 over_el = do
# # # #             counts+=1
# # # #         over_el = nums[do[0]-1:]
# # # #         if len(over_el) == do[0]:
# # # #             bools = False
# # # #
# # # # jump([2,3,1,1,4])
# # #
# # # def jump(nums: list[int]) -> int:
# # #     n = len(nums)
# # #     jumps = 0         # Количество прыжков
# # #     current_end = 0   # Текущая граница прыжка
# # #     farthest = 0      # Самая дальняя позиция, до которой можно допрыгнуть
# # #
# # #     for i in range(n - 1):
# # #         # Обновляем самую дальнюю достижимую позицию
# # #         farthest = max(farthest, i + nums[i])
# # #
# # #         # Если мы достигли текущей границы прыжка
# # #         if i == current_end:
# # #             jumps += 1              # Увеличиваем счётчик прыжков
# # #             current_end = farthest  # Обновляем границу для следующего прыжка
# # #
# # #             # Если уже достигли конца или дальше прыгать не нужно
# # #             if current_end >= n - 1:
# # #                 break
# # #
# # #     return jumps
# # # jump([2,3,1,1,4])
# #
# # # def jump(nums: list[int]) -> int:
# # #     n = len(nums)
# # #     jumps = 0         # Количество прыжков
# # #     current_end = 0   # Текущая граница прыжка
# # #     farthest = 0      # Самая дальняя позиция, до которой можно допрыгнуть
# # #
# # #     for i in range(n - 1):
# # #         # Обновляем самую дальнюю достижимую позицию
# # #         farthest = max(farthest, i + nums[i])
# # #
# # #         # Если мы достигли текущей границы прыжка
# # #         if i == current_end:
# # #             jumps += 1              # Увеличиваем счётчик прыжков
# # #             current_end = farthest  # Обновляем границу для следующего прыжка
# # #
# # #             # Если уже достигли конца или дальше прыгать не нужно
# # #             if current_end >= n - 1:
# # #                 break
# # #
# # #     return jumps
# # # print(jump([2,3,1,1,4]))
# #
# # # def two_numbers(lists,travle):
# # #     for i in range(len(lists)):
# # #         for j in range(len(lists)):
# # #             if lists[i] + lists[j] == travle and i != j:
# # #                 return i,j
# # # print(two_numbers([2,7,11,15],9))
# # #
# #
# # # def twoSum(self, nums, target: int):
# # #     saype = {}
# # #     for i in range(len(num)):
# # #         saype[nums[i]] = i
# # #     for i in range(len(num)):
# # #         over_el = target - saype[num[i]]
# # #         if over_el in saype and i != saype[i]:
# # #             return i, saype[i]
# #
# # def addTwoNumbers(l1, l2):
# #     l1 = l1[::-1]
# #     l2 = l2[::-1]
# #     print(l1,l2)
# #     l1 = [str(i) for i in l1]
# #     l2 = [str(i) for i in l2]
# #     over_el = sum(l1,l2)
# #     over_el = over_el[::-1]
# #     l1 = [int(i) for i in over_el]
# #     return l1
# # print(addTwoNumbers([2,4,3] ,   [5,6,4]))
# #
# # def mergeTwoLists(list1, list2):
# #     over_el = {}
# #     counts = 0
# #     while counts < (len(list1) + len(list2)):
# #         if len(list1) and len(list2) >= 2:
# #             if list1 > list2:
# #                 over_el[counts] = list1[counts]
# #                 counts -= 1
# #             elif list1 < list2:
# #                 over_el[counts] = list2[counts]
# #             else:
# #                 pass
# #         else:
# #             return over_el
# #         counts += 1
# #     return over_el
# # print(mergeTwoLists([[1,2,4]],[[1,3,4]]))
#
# dicts = {}
# lists = [2,3,4,5,6,7]
# for i in range(10):
#     dicts.update(i=lists[i])
#
# print(dicts)