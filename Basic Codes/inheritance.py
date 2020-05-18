class UserData():
    age = 0
    name = None
    def __init__(self, name, age):
        self.name = name
        self.age = age

user1 = UserData('Sara', 40)
user2 = UserData('Greg', 25)
print(user1.name)
    
class phoneNumber(UserData):
    def __init__(self, name, age, num):
        super().__init__(name, age)
        self.num = num

user1 = phoneNumber('Sara', 40, 757496734)
user2 = phoneNumber('Greg', 25, 727834123)

print(user2.num)
