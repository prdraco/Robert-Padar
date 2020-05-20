#Define a simple class for fruits:
class fruits():
    def mediterran(self):
        x= ''
        print('Orange, Pineaple, Mango')
        return x
    def european(self):
        y= ''
        print('Apple, pear, strawberry, blueberry, grapes')
        return y

fruits.european(print)
fruits.mediterran(print)

# constructor method
class UserData():
    name = None
    age = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def user(self):
        print('User name is: {} and has {} years old!' .format(self.name, self.age))
    def __len__(self):
        return self.age

user1 = UserData('Sara', '40')
user2 = UserData('Robert', '40')
user3 = UserData('Roland', '24')
user4 = UserData('Anita', '37')
UserData.user(user1)
UserData.user(user2)
UserData.user(user3)
UserData.user(user4)

print(user2.age)