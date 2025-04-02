import pickle
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def make_sound(self):
        return "Чирик!"

    def eat(self):
        return f"{self.name} ест семена."

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        return "Рррр!"

    def eat(self):
        return f"{self.name} ест мясо."

class Reptile(Animal):
    def __init__(self, name, age, is_poisonous):
        super().__init__(name, age)
        self.is_poisonous = is_poisonous

    def make_sound(self):
        return "Шшшш!"

    def eat(self):
        return f"{self.name} ест насекомых."

def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, employee):
        self.staff.append(employee)

    def save_to_file(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def load_from_file(cls, filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)

class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}. {animal.eat()}")

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")

# Пример использования
if __name__ == "__main__":
    # Создаем зоопарк
    zoo = Zoo()

    # Добавляем животных
    zoo.add_animal(Bird("Воробья", 2, 15))
    zoo.add_animal(Mammal("Льва", 5, "Golden"))
    zoo.add_animal(Reptile("Змея", 3, True))

    # Добавляем сотрудников
    keeper = ZooKeeper("Петя")
    vet = Veterinarian("Люся")
    zoo.add_staff(keeper)
    zoo.add_staff(vet)

    # Демонстрация полиморфизма
    animal_sound(zoo.animals)

    # Работа сотрудников
    keeper.feed_animal(zoo.animals[0])
    vet.heal_animal(zoo.animals[1])

    # Сохраняем зоопарк в файл
    zoo.save_to_file("my_zoo.pkl")

    # Загружаем зоопарк из файла
    loaded_zoo = Zoo.load_from_file("my_zoo.pkl")
    print("\nПосле загрузки из файла:")
    animal_sound(loaded_zoo.animals)