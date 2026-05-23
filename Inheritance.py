class Person:
        def __init__(self, name):
            self.name = name

        def talk(self):
            print(f"Hi {self.name} Welcome Onboard")


employee = Person("Anusha")
employee.talk()
