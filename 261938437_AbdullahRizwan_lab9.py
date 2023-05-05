class Person:
    def __init__(self, name, age):
        self.name= name
        self.age= age

    def Display(self):
        print("Name:",self.name)
        print("Age:",self.age)

class House:
    def __init__(self, address, no_of_rooms):
        self.address = address
        self.rooms = no_of_rooms
        self.people_living_inside = []

    def Display(self):
        print("Address:", self.address)
        print("Number of rooms:", self.rooms)
        print("The following people are living in this house:")
        for x in self.people_living_inside:
            x.Display()

    def Add_person(self, person):
        self.people_living_inside.append(person)

    def Remove_person(self, person):
        self.people_living_inside.remove(person)

p1= Person("Aima",18)
h1 =House("falcon",5)

h1.Add_person(p1)
h1.Display()
