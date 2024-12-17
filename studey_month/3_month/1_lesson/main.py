# import json
# data = """[{"userId": 1,"id": 1,"title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"},{"userId": 1,"id": 2,"title": "qui est esse"}]"""
# date_baze = json.loads(data)
# for i in date_baze:
#     if "s" in i["title"]:
#         print("hello")
#     else:
#         print("hello 5")

import requests
import json

date = requests.get("https://jsonplaceholder.typicode.com/posts").json()

counts = 1
for i in date:
    dates = requests.get(f"https://jsonplaceholder.typicode.com/posts/{counts}").json()
    counts += 1
    print(dates)
def Updat_every_body(arg):
    counts = 0
    for i in arg:
        counts += 1
        i["body"] = f"hello sardor {counts}"
        i["title"] = f"Akobirov {counts}"
        print(i)


Updat_every_body(date)