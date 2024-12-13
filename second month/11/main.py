from tkinter.font import names


class User :
    def __init__(self):
        self.name = {}
    def __getitem__(self, item):
        return f"name is {self.name.get(item, "juk !!!")}"

    def __setitem__(self, key, value):
        if type(self.name[key]) == int:
            self.name[key] = value * 2
        else:
            return "hello"
        return self.name

    def __delitem__(self, key):
        if key in self.name:
            print(f"{key} del buladi !!!")
            del self.name[key]
        else:
            print("malumot yuk")

    def __len__(self):
        if len(self.name) == 4:
            return len(self.name)-1
        else:
            return len(self.name)+1
user1 = User()
user1.name["name"] = 2
user1.name["name2"] = 2
user1.name["name3"] = 2
user1.name["name4"] = 2
print(user1.__len__())
# print(user1.__setitem__("name",2))
# print(user1.__delitem__("name1"))
# print(user1.__delitem__("name1"))
# print(user1["name2"])


