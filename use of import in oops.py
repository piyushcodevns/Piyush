import oops as oops

class Person:
    def __init__(self, name, age, address, mybook):
        self.name = name
        self.age = age
        self.address = address
        self.mybook = mybook

    def __str__(self):
        return "name={0}, age={1}, address={2}, mybook={3}".format(
            self.name, self.age, self.address, self.mybook
        )
b1 = oops.Regression("Python", "Ravi", 500, "Programming")
p = Person("Piyush", 18, "Varanasi", b1)
print(p)