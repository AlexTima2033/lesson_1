class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def play(self):
        print(f"{self.name} сейчас играет.")
    def cat_passport(self):
        print(f"Это {self.name}, и ему {self.age} лет.")

class Dog(Cat):
    def __init__(self, name, age):
        super().__init__(name, age)

my_dog = Dog(name="Reks", age=20)
print(my_dog.name)
print(my_dog.age)
my_dog.play()

my_cat = Cat(name="Barsik", age=10)
my_cats = Cat("Murzik", 5)
print(my_cat.name)
print(my_cat.age)
my_cat.play()
my_cat.cat_passport()
my_cats.play()
my_cats.cat_passport()