# # # def func(a, b, *args, **kwargs):
# # #     print(a, b, args, kwargs)
# # #
# # #
# # # func(1, 2, 3, "salom", 5, 6, name="dilshod", lastname="murtazoyev")
# # #
# # # # dicts = {
# # # #     "name": "sardor"
# # # # }
# # # # print(dicts.items())
# # # # dicts.update(surname="rodras")
# # # # print(dicts.items())
# # # # print(dicts.keys())
# # # def last_strs(arg: list[str]) -> str:
# # #     if not arg:
# # #         return ""
# # #     over_el = arg[0]
# # #     for i in arg[1:]:
# # #         while not i.startswith(over_el):
# # #             over_el = over_el[:-1]
# # #             if not over_el:
# # #                 return ""
# # #     return over_el
# # # print(last_strs(["flower","flow","flight"]))
# #
# # # def reomve_lishniy(arg: list[int]) -> int:
# # #     arg = sorted(arg)
# # #     if not arg:
# # #         return 0
# # #     i = 0
# # #     for j in range(1,len(arg)):
# # #         if arg[j] != arg[i]:
# # #             i += 1
# # #             arg[i] = arg[j]
# # #     return i + 1
# # nums     = [1,2,3,4,4,4,4,8,4]
# # counts = 0
# # if not nums:
# #     return 0
# # while counts < len(num):
# #     if num[counts] == val:
# #         del num[counts]
# #         counts -= 1
# #     counts += 1
# # return num
#
# nums = [1,1,2,3,4,5,5,5,6,6,6]
# counts = 0
# while counts < len(nums):
#     if nums[counts] == 4:
#         del nums[counts]
#         counts -= 1
#
#     counts+=1
# print()