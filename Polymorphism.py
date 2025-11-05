class cat :
    def __init__ (self, name, age) :
        self.name = name
        self.age = age
        print(f"Hello, I am {self.name} and I am {self.age} years old.")
    def speak(self) :
        return "Meow"
    
class dog : 
    def __init__ (self, name, age) :
        self.name = name
        self.age = age
        print(f"Hello, I am {self.name} and I am {self.age} years old.")
    def speak(self) :
        return "Woof"
    
def animal_sound(animal) :
    print(animal.speak())
    print(animal.sound())




cat1 = cat("Whiskers", 3)
dog1 = dog("Buddy", 5)
