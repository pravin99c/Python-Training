# 2.Create classes according to the following class map
# ->  Animal => Wild => Leopard, Tiger
# 	=> Pet => Dog
# 	=> Canine => Fox
# -> Each class contains two methods to get a name and info. Get the name returns the name of that animal and get the info returns hierarchy.
# For example,
# print(dog.get_name())  ⇒ My name is Tommy
# print(dog.get_info())  ⇒  I am Dog. I am Pet. I am Animal


class Animal():
    def get_info(self):
        return "I am Animal"
class Wild(Animal):
    def get_info(self):
        return "I am {}. {}".format("Wild",Animal.get_info(self))
class Pet(Animal):
    def get_info(self):
        return "I am {}. {}".format("Pet",Animal.get_info(self))
class Canine(Animal):
    def get_info(self):
        return "I am Canine. {}".format(Animal.get_info(self))
class Leopard(Wild):
    def __init__(self,name):
        self.name=name
    def get_name(self):
        return "I am {}".format(self.name)
    def get_info(self):
        return "I am {}. {}".format(self.name,Wild.get_info(self))
class Tiger(Wild):
    def __init__(self,name):
        self.name=name
    def get_name(self):
        return "I am {}".format(self.name)
    def get_info(self):
        return "I am {}. {}".format(self.name,Wild.get_info(self))
class Dog(Pet):
    def __init__(self,name):
        self.name=name
    def get_name(self):
        return "I am {}".format(self.name)
    def get_info(self):
        return "I am {}. {}".format(self.name,Pet.get_info(self))
class Fox(Canine):
    def __init__(self,name):
        self.name=name
    def get_name(self):
        return "I am {}".format(self.name)
    def get_info(self):
        return "I am {}. {}".format(self.name,Canine.get_info(self))
fox=Fox("Fox")
print(fox.get_name())
print(fox.get_info(),end="")
print()

dog=Dog("Tommay")
print(dog.get_name())
print(dog.get_info(),end="")
print()

leopard=Leopard("leopard")
print(leopard.get_name())
print(leopard.get_info(),end="")
print()

tiger=Tiger("tiger")
print(tiger.get_name())
print(tiger.get_info(),end="")
print()