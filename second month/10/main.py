class User:
    name = None
    surname = None
    age = None
    level_in_game = None

    def __init__(self , name , surname , age , level ):
        name = self.name
        surname = self.surname
        age = self.age
        level = self.level_in_game


user_1 = User("sardor","akobirov",16,15)

print(user_1)