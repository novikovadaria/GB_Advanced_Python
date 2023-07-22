class Cat:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def speak(self):
        return "Meow"

class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def speak(self):
        return "Woof"

class AnimalFactory:
    def create_animal(self, animal_type, name, breed, age):
        if animal_type.lower() == "cat":
            return Cat(name, breed, age)
        elif animal_type.lower() == "dog":
            return Dog(name, breed, age)
        else:
            raise ValueError("Invalid animal type")
        
# Использование класса
factory = AnimalFactory()

cat = factory.create_animal("cat", "Fluffy", "Persian", 3)
dog = factory.create_animal("dog", "Buddy", "Golden Retriever", 5)

print(cat.speak())  # Выводит: "Meow"
print(dog.speak())  # Выводит: "Woof"