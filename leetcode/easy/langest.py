# def langesFirst(strs: list[str]) -> str:
#     if not strs:
#         return  ""
#     osnowa = strs[0]
#     for i in strs[1:]:
#         while not i.startswith(osnowa):
#             osnowa = osnowa[:-1]
#             if not osnowa:
#                 return ""
#     return osnowa
# print(langesFirst(["dog","racecar","car"]))

