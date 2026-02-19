"""Method overriding: same method name, different behavior."""

class Parent:
    def hello(self):
        print("I`m an adult")

class Child(Parent):
    def hello(self):
        print("I`m a child")

if __name__ == "__main__":
    p = Parent()
    c = Child()
    p.hello()
    c.hello()
