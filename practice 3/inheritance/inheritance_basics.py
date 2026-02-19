"""Inheritance basics: Animal -> Dog."""
class Animal:
    def speak(self):
        print("Some sound...")

class Dog(Animal):
    def speak(self):
        print("Woof!")

if __name__ == "__main__":
    a = Animal()
    d = Dog()
    a.speak()
    d.speak()
