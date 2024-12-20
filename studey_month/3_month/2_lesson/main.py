# # # # # import requests
# # # # # import json
# # # # #
# # # # # def translater(arg):
# # # # #     date = requests.get(f"https://translate.google.com/?hl=ru&sl=ru&tl=en&text={arg}&op=translate").json()
# # # # #     print(date)
# # # # #
# # # # #
# # # # # translater("сардор")
# # # #
# # # # import requests
# # # #
# # # # API_KEY = '4e80693c-f179-4e4d-ac1c-f1f3f6f0a412'
# # # # url = "https://translate.api.cloud.yandex.net/translate/v2/translate"
# # # #
# # # # headers = {
# # # #     "Authorization": f"Api-Key {API_KEY}"
# # # # }
# # # #
# # # # data = {
# # # #     "targetLanguageCode": "ru",
# # # #     "texts": ["Hello, world!"],
# # # #     "folderId": "your_folder_id"
# # # # }
# # # #
# # # # response = requests.post(url, json=data, headers=headers)
# # # #
# # # # if response.status_code == 200:
# # # #     translated_text = response.json()['translations'][0]['text']
# # # #     print("Переведенный текст:", translated_text)
# # # # else:
# # # #     print("Ошибка:", response.text)
# # #
# # # from googletrans import Translator
# # #
# # # def tranlatorss(arg, county):
# # #     translator = Translator()
# # #     perevod = translator.translate(arg,dest=f"{county}")
# # #     return perevod.text
# # #
# # # x = input("add the text:: ")
# # # l = input("add the lenguage:: ")
# # #
# # # print(tranlatorss(x,l))
# # from itertools import count
#
# # import requests
# #
# # def Translater():
# #     url = "https://google-translate113.p.rapidapi.com/api/v1/translator/html"
# #
# #     froms = input("add the lenguage you use")
# #     to = input("add the lenguage you want to translate")
# #     body = input("add the text")
# #
# #     information = {
# #         "from": froms,
# #         "to": to,
# #         "html": body
# #     }
# #
# #     headers = {
# #         "x-rapidapi-key": "315ff47081mshe2a2e6af908f97ep129cfajsn34409205edf6",
# #         "x-rapidapi-host": "google-translate113.p.rapidapi.com",
# #         "Content-Type": "application/json"
# #     }
# #
# #     response = requests.post(url, json=information, params=headers)
# #
# #     print(response.status_code)
# # Translater()
#
# import requests
# url = "https://google-translate113.p.rapidapi.com/api/v1/translator/html"
#
# froms = input("add the lenguage you use:: ")
# to = input("add the lenguage you want to translate:: ")
# body = input("add the text:: ")
#
# payload = {
# 	"from": froms,
# 	"to": to,
# 	"html": body
# }
# headers = {
# 	"x-rapidapi-key": "315ff47081mshe2a2e6af908f97ep129cfajsn34409205edf6",
# 	"x-rapidapi-host": "google-translate113.p.rapidapi.com",
# 	"Content-Type": "application/json"
# }
#
# response = requests.post(url, json=payload, headers=headers)
#
# print(response.json())