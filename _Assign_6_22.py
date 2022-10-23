# 1. Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. 
# You must perform the following operations:

#  a. It should have a function ‘description()’ which prints the name and age of the dog.
#  b. It should have a function ‘get_info()’ which prints the coat color of the dog.
#  c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’. It should have at least two methods of its own.
#  d. Create objects and implement the above functionalities.


class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
    
    def description(self):
        print("name :",self.name)
        print("age: ",self.age,"years")
    
    def get_info(self):
        print("coat color: ",self.coat_color)

class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color, origin, weight):
        super().__init__(name, age, coat_color)
        self.origin= origin
        self.weight = weight

    def Originated(self):
        print("Origin: ", self.origin)
    
    def Weightage(self):
        print("Weight :", self.weight,"\n")

class Bulldog (Dog):
    def __init__(self, name, age, coat_color, origin_1, weight_1):
        super().__init__(name, age, coat_color)
        self.origin_1=origin_1
        self.weight_1=weight_1

    def Originated_1(self):
        print("Origin : ",self.origin_1)
    
    def Weightage_1(self):
        print("Weight: ",self.weight_1)

print("\nDogs Info. as follows -\n")   #<<< optional

JackRuss_Obj = JackRussellTerrier("JackRussellTerrier", 14.5 ," White, White & Tan, Black & White","England", "6 to 8 kg (Adult)")
JackRuss_Obj.description()
JackRuss_Obj.get_info()
JackRuss_Obj.Originated()
JackRuss_Obj.Weightage()


Bulldog_Obj = Bulldog("Bulldog", 9 , " White, Fawn, Piebald, Fawn & White, Brindle & White, Red, Red & White, Red Brindle", " British Isles","18 to 25 kg")
Bulldog_Obj.description()
Bulldog_Obj.get_info()
Bulldog_Obj.Originated_1()
Bulldog_Obj.Weightage_1()







