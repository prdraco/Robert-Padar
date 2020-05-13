#Create a new Book class with a constructor method that 
# will receive two attribute values when an object is 
# created from the class, the book's title and author;
#Within the class definition, set the title attribute to a 
# private attribute, and create a property with a method that 
# will provide indirect access to the private title attribute;
#Provide write access to the private attribute to enable the 
# book object's title to be changed and reject the change if 
# an empty string is provided as the new title;
#Create a new novel object with the title attribute set to 
# "The Fix" and the author attribute set to "David Baldacci", 
# and print the object's title and author;
#Invoke the method which will change the book's title and change it 
# to "The Last Mile"; then try changing the title to an emprty string.

class book(object):
    def __init__(self, __title, author):
        self.__title = __title
        self.author = author
    @property
    def title(self):
        return self.__title
    @title.setter	
    def title(self, new_title):
        if new_title == "":
            print("\nAn title name can't be an empty string.")
        else:
            self.__title == new_title
            print("Title changed successful!")

novel = book("The Fix", "David Bajdacci")
print("\nBefore change!")
print(novel.title)
print(novel.author)

print("\nAfter change!")

novel.__title = "The Last Mile"
print(novel.__title)

novel.title = ""