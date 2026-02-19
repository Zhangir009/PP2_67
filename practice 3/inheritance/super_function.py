class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def describe(self) -> str:
        return f"{self.name} earns {self.salary}."


class Developer(Employee):
    def __init__(self, name: str, salary: float, language: str):
        super().__init__(name, salary)  # call parent constructor
        self.language = language

    def describe(self) -> str:
        # Reuse parent method using super()
        base = super().describe()
        return f"{base} Favorite language: {self.language}."


if __name__ == "__main__":
    # Example 1: parent
    e = Employee("Aibek", 2000)
    print(e.describe())

    # Example 2: child uses super() to initialize name/salary
    dev = Developer("Dana", 3000, "Python")
    print(dev.describe())

    # Example 3: child still has inherited attributes
    print("dev name:", dev.name, "| dev salary:", dev.salary)

    # Example 4: and extra child attribute
    print("dev language:", dev.language)