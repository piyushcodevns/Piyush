class Father:
    def skills(self):
        print("Father: Gardening, Cooking")

class Mother:
    def skills(self):
        print("Mother: Painting, Dancing")

class Child(Father, Mother):
    pass

c = Child()
c.skills()  
print(Child.mro())