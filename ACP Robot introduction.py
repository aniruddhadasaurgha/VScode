class robot :
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print(f"Hello, my name is {self.name}. I am {self.color} and weigh {self.weight} kg.")
class humanoid(robot):
    def __init__(self, name, color, weight, language):
        super().__init__(name, color, weight)
        self.language = language

    def greet(self):
        print(f"I can speak {self.language}.")
class android(robot):
    def __init__(self, name, color, weight, model):
        super().__init__(name, color, weight)
        self.model = model

    def show_model(self):
        print(f"My model is {self.model}.")
r1 = humanoid("Alice", "silver", 70, "English")
r2 = android("Bob", "black", 80, "XJ-9")
r1.introduce_self()
r1.greet()
r2.introduce_self()
r2.show_model()


