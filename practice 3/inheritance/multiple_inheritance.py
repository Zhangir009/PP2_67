"""Multiple inheritance (very simple) + MRO demonstration."""

class Flyer:
    def move(self):
        print("I fly")

class Swimmer:
    def move(self):
        print("I swim")

class Duck(Flyer, Swimmer):
    pass

if __name__ == "__main__":
    d = Duck()
    d.move()  # Flyer first because Duck(Flyer, Swimmer)

    print("Duck MRO:", [cls.__name__ for cls in Duck.mro()])