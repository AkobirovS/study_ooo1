# # # # # # import json
# # # # # # data = """[{"userId": 1,"id": 1,"title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"},{"userId": 1,"id": 2,"title": "qui est esse"}]"""
# # # # # # date_baze = json.loads(data)
# # # # # # for i in date_baze:
# # # # # #     if "s" in i["title"]:
# # # # # #         print("hello")
# # # # # #     else:
# # # # # #         print("hello 5")
# # # # #
# # # # # import requests
# # # # # import json
# # # # #
# # # # # date = requests.get("https://jsonplaceholder.typicode.com/posts").json()
# # # # #
# # # # # counts = 1
# # # # # for i in date:
# # # # #     dates = requests.get(f"https://jsonplaceholder.typicode.com/posts/{counts}").json()
# # # # #     counts += 1
# # # # #     print(dates)
# # # # # def Updat_every_body(arg):
# # # # #     counts = 0
# # # # #     for i in arg:
# # # # #         counts += 1
# # # # #         i["body"] = f"hello sardor {counts}"
# # # # #         i["title"] = f"Akobirov {counts}"
# # # # #         print(i)
# # # # #
# # # # #
# # # # # Updat_every_body(date)
# # # #
# # # #
# # # #
# # # #
# # # # #
# # # # # import requests
# # # # # API_TOKEN = "bc5758be47068c23e9c0f6adf5cab5c9"
# # # # #
# # # # #
# # # # # parans = {"q":"londan" , "appid":API_TOKEN}
# # # # #
# # # # # date = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parans)
# # # # #
# # # # # print(date.text)
# # # # #
# # # # #
# # # #
# # #
# # # import requests
# # #
# # # API_TOKEN = "bc5758be47068c23e9c0f6adf5cab5c9"
# # #
# # # params = {"q": "london", "appid": API_TOKEN}
# # #
# # # response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)
# # #
# # # if response.status_code == 200:
# # #     print(response.json())
# # # else:
# # #     print(f"Ошибка: {response.status_code}")
# # #
# # # data = response.json()
# # # print(type(data))
# # #
# # #
# # #
# # # import requests
# # #
# # # params = {"q":"fanny cats"}
# # #
# # # # information = requests.get("https://diyarelsalam.com")
# # #
# # # # print(information.text)
# # from itertools import permutations
# # from bs4 import BeautifulSoup
# # import requests
# # import random
# # import time
# #
# # def weather_check(city):
# #
# #     user_agents = [
# #         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
# #         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
# #         "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
# #         "Mozilla/5.0 (iPhone; CPU iPhone OS 13_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Mobile/15E148 Safari/604.1"
# #     ]
# #
# #     headers = {
# #         "User-Agent": random.choice(user_agents)
# #     }
# #
# #     url = f"https://www.google.com/search?q=weather+in+{city}"
# #     res = requests.get(url, headers=headers)
# #
# #     if res.status_code == 200:
# #         soup = BeautifulSoup(res.text, "html.parser")
# #         try:
# #             time = soup.select("#wob_dts")[0].getText().strip()
# #             precipitation = soup.select("#wob_dc")[0].getText().strip()
# #             temperature = soup.select("#wob_tm")[0].getText().strip()
# #
# #             print(f"""Day and Time: {time}
# # Precipitation: {precipitation}
# # Temperature: {temperature}°C""")
# #
# #         except IndexError:
# #             print("Не удалось получить информацию о погоде. Проверьте правильность введенного города.")
# #     else:
# #         print(f"Ошибка запроса: {res.status_code}")
# #
# # if __name__ == "__main__":
# #     city_input = input("Add the name of the city: ")
# #     weather_check(city_input)
# #     time.sleep(5)
#
# import requests
#
#
# def get_weather(city):
#     API_KEY = "bc5758be47068c23e9c0f6adf5cab5c9"  # Вставьте сюда ваш API-ключ
#     BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
#
#     params = {
#         "q": city,
#         "appid": API_KEY,
#         "units": "metric",  # Получаем температуру в градусах Цельсия
#         "lang": "ru"  # Локализация на русский язык
#     }
#
#     response = requests.get(BASE_URL, params=params)
#
#     if response.status_code == 200:
#         data = response.json()
#         city_name = data["name"]
#         temperature = data["main"]["temp"]
#         weather_description = data["weather"][0]["description"]
#         humidity = data["main"]["humidity"]
#         wind_speed = data["wind"]["speed"]
#
#         print(f"Погода в городе: {city_name}")
#         print(f"Температура: {temperature}°C")
#         print(f"Описание: {weather_description}")
#         print(f"Влажность: {humidity}%")
#         print(f"Скорость ветра: {wind_speed} м/с")
#     elif response.status_code == 404:
#         print("Город не найден. Проверьте правильность названия.")
#     else:
#         print(f"Ошибка запроса: {response.status_code}")
#
#
# if __name__ == "__main__":
#     city_input = input("Введите название города: ")
#     get_weather(city_input)
