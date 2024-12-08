# # def RemoveElemen(arg_1: list[int],arg_2: int) -> list:
# #     over_len = len(arg_1)-1
# #     counts = 0
# #     while over_len > counts:
# #         if arg_1[counts] == arg_2:
# #             arg_1.remove(arg_1[counts])
# #             counts -= 1
# #         else:
# #             counts+=1
# #
# #
# #     return arg_1
# # print(RemoveElemen([1,2,3,4,4,4,4,8,4],4))
# from itertools import count
# from time import process_time_ns
#
#
# # lists = [1,2,3,4,4,4,4,8,4]
# # i = 0
# # while i < len(lists):
# #     if lists[i] == 4:
# #         del lists[i]
# #     i +=1
# # print(lists)
# #
# # def strStr(haystack: str, needle: str) -> int:
# #     if needle in haystack:
# #         first_over = haystack.index(needle[0])
# #         count = first_over + 1
# #         while count < len(haystack):
# #             if haystack[count] == needle[-1]:
# #                 if haystack[first_over:count + 1] == needle:
# #                     return 0
# #             count += 1
# #
# #         return first_over
# #     else:
# #         return -1
# #
# # print(strStr("mississippi","issip"))
# #
# # def strStr(haystack, needle):
# #     len_h = len(haystack)
# #     len_n = len(needle)
# #
# #     for i in range(len_h - len_n + 1):
# #         print(len_h - len_n)
# #         if haystack[i:i + len_n] == needle:
# #             return i
# #
# #     return -1
# # #
# # #
# # # print(strStr("sadbutsad", "sad"))  # Вывод: 0
# # # print(strStr("leetcode", "leeto"))  # Вывод: -1
# # def bynarySearch(nums: list[int] , target: int):
# #     if min(nums) >= target:
# #         return 0
# #     if target in nums:
# #         right = len(nums)-1
# #         low = 0
# #         while right > low:
# #             mid = (right + low) // 2
# #             if nums[mid] == target:
# #                 return mid
# #             elif mid > target:
# #                 right = low + mid
# #             else:
# #                 low = right - mid
# #     else:
# #         listsMin = []
# #         for i in nums:
# #             if i < target:
# #                 listsMin.append(i)
# #         return nums.index(max(listsMin)) + 1
# #
# # print(bynarySearch([1,3,5,6] , 5))
# # print(bynarySearch([1,4,6,7,8,9] , 6    ))
#
# def bynarySearch(nums: list[int] , target: int):
#     right = len(nums) - 1
#     low = 0
#     while low <= right:
#         mid = (right + low) // 2
#         if nums[mid] == target:
#             return mid
#         elif mid > target:
#             right = low - 1
#         else:
#             low = right +   1
# print(bynarySearch([1,4,6,7,8,9] , 3))
#
#
# def searchInsert(nums, target):
#     left = 0
#     right = len(nums) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] > target:
#             right = mid - 1
#         else:
#             left = mid + 1
#
#     return left
#
#
# # Примеры
# print(searchInsert([1, 3, 5, 6], 5))  # Вывод: 2
# print(searchInsert([1, 3, 5, 6], 2))  # Вывод: 1
# print(searchInsert([1, 3, 5, 6], 7))  # Вывод: 4
