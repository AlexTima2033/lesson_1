class Cat:
    def __init__(self, name, age, eat, toy):
        self.name = name
        self.age = age
        self.eat = eat
        self.toy = toy

    def passport(self):
        print(f"Это {self.name}, и ему {self.age} лет.")

    def nutrition(self):
        print(f"Это {self.name} питается {self.eat}.")

    def favorite_toy(self):
        print(f"Это {self.name}, его любимая игрушка - {self.toy}.")

my_cat = Cat(name="Jastin", age=5, eat="dry_food", toy="ball")
my_cats = Cat(name="Mars", age=10, eat="natural_food", toy="mouse")

my_cat.passport()
my_cat.nutrition()
my_cat.favorite_toy()

my_cats.passport()
my_cats.nutrition()
my_cats.favorite_toy()

class Dog(Cat):
    def __init__(self, name, age, eat, toy):
        super().__init__(name, age, eat, toy)

my_dog = Dog(name="Reks", age=20, eat="meat", toy="bone")

my_dog.passport()
my_dog.nutrition()
my_dog.favorite_toy()


