# # datetime detime
# # def fibanachhi(c: int,a=0, b=1,count=0):
# #     ab = a + b
# #     if c < 2:
# #         return ab
# #     elif ab < c:
# #         print(ab)
# #         ab = a * b
# #         return fibanachhi(c,b,ab)
# #     else:
# #         pass
# #
# #
# # print(fibanachhi(4))
#
# # def fackterial(c: int,a=1,ower=0):
# #     ab = a * a+1
# #     if c < 2:
# #         return None
# #     elif a <= c:
# #         a += 1
# #         print(a)
# #         print(ower, "anime")
# #         return fackterial(c,a, ab)
# #     else:
# #         pass
# # print(fackterial(4))
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # def factorial(n: int) -> int:
# #     if n == 0 or n == 1:
# #         return 1
# #     return n * factorial(n - 1)
# #
# # print(factorial(5))
# #
# #
#
#
# import requests
# import pandas as pd
#
# date = requests.get("https://dummyjson.com/users").json()
# date = date["users"]
# hear = []
# for i in date:
#     hear.append(i["hair"])
#     print(i["hair"])
#     del i["hair"]
#
# for i in hear
#
# # date2 = pd.DataFrame(date)
# # date2.to_excel("1313.xlsx")
# # print(date)


import requests

a = requests.get("https://app.cerebry.co/login").text

print(a)