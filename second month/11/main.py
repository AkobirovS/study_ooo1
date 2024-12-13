# from tkinter.font import names
#
#
# class User :
#     def __init__(self):
#         self.name = {}
#     def __getitem__(self, item):
#         return f"name is {self.name.get(item, "juk !!!")}"
#
#     def __setitem__(self, key, value):
#         if type(self.name[key]) == int:
#             self.name[key] = value * 2
#         else:
#             return "hello"
#         return self.name
#
#     def __delitem__(self, key):
#         if key in self.name:
#             print(f"{key} del buladi !!!")
#             del self.name[key]
#         else:
#             print("malumot yuk")
#
#     def __len__(self):
#         # if len(self.name) == 4:
#         #     return len(self.name)-1
#         # else:
#         #     return len(self.name)+1
#         return len(self.name)
# user1 = User()
# user1.name["name"] = "sardor"
# user1.name["name2"] = 2
# user1.name["name3"] = 2
# user1.name["name4"] = 2
# print(user1.name["name"].__len__())
# # print(user1.__setitem__("name",2))
# # print(user1.__delitem__("name1"))
# # print(user1.__delitem__("name1"))
# # print(user1["name2"])
#
#


class Cats:
    Name = ""
    Types = ""
    Age = None
    def __init__(self,name,types,age):
        self.Name = name
        self.Types = types
        self.Age = age
        self.kittens = {}

    def __call__(self, *args, **kwargs):
        overEl = {}
        for i in range(len(args)):
            overEl[i] = args[i]
            print(f"pleace use these {overEl.items()} and in Init !!!")
        return "!!!!  pleace  !!!!!"

    def __repr__(self):
        return "maybe this have one anothe avanue for kittens"

    def __str__(self):
        return f"Hi this shop for get Cats an\nfirst by first add your cat information\nif your cat have kitten use the __setitem__\nif do you want to know , do suit you kitten us use __getitem__\nuse the __len__ for get you money"

    def __del__(self):
        print("we get onle 10 or younger years old cats !!")
        if self.Age > 10:
            print(f"this cat does not suit us {self.Name}")
            del self.Name
            del self.Age
            del self.Types
            return "excusme for it !!"
        else:
            return "you cat suit us"

    def __setitem__(self, key, value):
        self.kittens[key] = value

    def __getitem__(self, item):
        if self.kittens[item] > 5:
            return "we are so sorry but\nyour kittens do not suit us"
        else:
            return "you kittens suit us"

    def __delitem__(self, key):
        onswer = input("does not you want to give your kitten ? use y or n ::: ")
        if onswer == "n":
            del self.kittens[key]
            return "we delet this kitten"
        else:
            return "ok it is good for us thank you !!!"

    def __len__(self):
        lens = len(self.kittens)
        return f"we give you for kittens {lens}00$ and for your cat 100$"

cat1 = Cats("Alfa","zamurskie",7)
cat1.__setitem__("Alfamini",5)
cat1.__setitem__("sashka",2)
cat1.__setitem__("rijik",3)
# print(cat1.__getitem__("sashka"))
# print(cat1.__del__())
# print(len(cat1.kittens))
# print(cat1)
# print(cat1.__delitem__("sashka"))
print(cat1.__len__())
