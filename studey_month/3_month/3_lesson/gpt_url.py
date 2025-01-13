# # # # # # # # url = "https://zillow-working-api.p.rapidapi.com/autocomplete"
# # # # # # # import pandas
# # # # # # #
# # # # # # # a = pandas.read_excel("")]
# # # # # #
# # # # # #
# # # # # # def fibannachhi(a: int, b: int, c: int) -> int:
# # # # # #     if c == 1 :
# # # # # #         return a
# # # # # #     elif c == 2:
# # # # # #         return b
# # # # # #     else:
# # # # # #         counts = 3
# # # # # #         while counts <= c:
# # # # # #             a,b = b,a + b
# # # # # #             counts +=1
# # # # # #
# # # # # #         return b
# # # # # #
# # # # # #
# # # # # # print(fibannachhi(10,5,5))
# # # # #
# # # # #
# # # # # text = open("text.txt","w+",encoding="utf-8")
# # # # # text.write("sardorkhon!!!!")
# # # # # print(text.read())
# # # # # text.close()
# # # # #
# # # # # test = open("text.txt","r",encoding="utf-8")
# # # # #
# # # # # print(test.read())
# # # #
# # # # import pandas as pd
# # # #
# # # # data = {
# # # #     'Name': ['Ali', 'Sara', 'Omar'],
# # # #     'Age': [23, 25, 22],
# # # #     'City': ['Tashkent', 'Samarkand', 'Bukhara']
# # # # }
# # # #
# # # # df = pd.DataFrame(data)
# # # # print(df)
# # # #
# # # #
# # # # sardor = pd.read_excel('sardor.xlsx')
# # # # print(sardor)
# # # #
# # # #
# # # # import pandas as pd
# # # #
# # # # file_path = 'sardor.xlsx'
# # # # sheet_name = 'Sheet1'
# # # #
# # # # data = pd.read_excel(file_path, sheet_name=sheet_name)
# # # #
# # # # print("Текущие данные из Excel:")
# # # # print(data)
# # # #
# # # # new_data = {
# # # #     'Имя': ['Али', 'Фатима'],
# # # #     'Возраст': [20, 22],
# # # #     'Город': ['Ташкент', 'Москва']
# # # # }
# # # #
# # # # new_df = pd.DataFrame(new_data)
# # # #
# # # # data = pd.concat([data, new_df], ignore_index=True)
# # # #
# # # # data.to_excel(file_path, sheet_name=sheet_name, index=False)
# # # #
# # # # print("\nДанные успешно добавлены и сохранены!")
# # # #
# # # # # # # # url = "https://zillow-working-api.p.rapidapi.com/autocomplete"
# # # # # # # import pandas
# # # # # # #
# # # # # # # a = pandas.read_excel("")]
# # # # # #
# # # # # #
# # # # # # def fibannachhi(a: int, b: int, c: int) -> int:
# # # # # #     if c == 1 :
# # # # # #         return a
# # # # # #     elif c == 2:
# # # # # #         return b
# # # # # #     else:
# # # # # #         counts = 3
# # # # # #         while counts <= c:
# # # # # #             a,b = b,a + b
# # # # # #             counts +=1
# # # # # #
# # # # # #         return b
# # # # # #
# # # # # #
# # # # # # print(fibannachhi(10,5,5))
# # # # #
# # # # #
# # # # # text = open("text.txt","w+",encoding="utf-8")
# # # # # text.write("sardorkhon!!!!")
# # # # # print(text.read())
# # # # # text.close()
# # # # #
# # # # # test = open("text.txt","r",encoding="utf-8")
# # # # #
# # # # # print(test.read())
# # # #
# # # # import pandas as pd
# # # #
# # # # data = {
# # # #     'Name': ['Ali', 'Sara', 'Omar'],
# # # #     'Age': [23, 25, 22],
# # # #     'City': ['Tashkent', 'Samarkand', 'Bukhara']
# # # # }
# # # #
# # # # df = pd.DataFrame(data)
# # # # print(df)
# # # #
# # # #
# # # # sardor = pd.read_excel('sardor.xlsx')
# # # # print(sardor)
# # # #
# # # #
# # # # import pandas as pd
# # # #
# # # # file_path = 'sardor.xlsx'
# # # # sheet_name = 'Sheet1'
# # # #
# # # # data = pd.read_excel(file_path, sheet_name=sheet_name)
# # # #
# # # # print("Текущие данные из Excel:")
# # # # print(data)
# # # #
# # # # new_data = {
# # # #     'Имя': ['Али', 'Фатима'],
# # # #     'Возраст': [20, 22],
# # # #     'Город': ['Ташкент', 'Москва']
# # # # }
# # # #
# # # # new_df = pd.DataFrame(new_data)
# # # #
# # # # data = pd.concat([data, new_df], ignore_index=True)
# # # #
# # # # data.to_excel(file_path, sheet_name=sheet_name, index=False)
# # # #
# # # # print("\nДанные успешно добавлены и сохранены!")
# # # #
# # # #
# # #
# # # def addTwoNumbers(l1: list[list[]], l2: Optional[ListNode]) -> Optional[ListNode]:
# # #     list1 = [str(i) for i in l1]
# # #     list2 = [str(i) for i in l2]
# # #     # Соединяем строки, переворачиваем, переводим в число
# # #     num1 = int(''.join(list1)[::-1])
# # #     num2 = int(''.join(list2)[::-1])
# # #     # Складываем числа, переводим сумму в строку
# # #     str_ = str(num1 + num2)
# # #     # Переводим каждую цифру в число
# # #     lst_s = [int(i) for i in str_]
# # #     # Печатаем список чисел наоборот
# # #     print(lst_s[::-1])
# #
# # sardor = open("text.txt","w",encoding="utf-8")
# # sardor.write("sarodr")
# #
# # sardor.close()
# #
# # sardor2 = open("text.txt","r", encoding="utf-8")
# # print(sardor2.read())
# #
# # try:
# #     sardor3 = open("text1.txt","x")
# # except:
# #     print("это создан !")
# # print(sardor3)
# import json
#
# import requests
# date = requests.get("https://jsonplaceholder.typicode.com/posts").json()
# date2 = json.loads()
# print(date2)
