class Fruit:

# Constructor

    def __init__(self, name, color):

    self.name = name

    self.color = color

print(f"{self.name} created with color {self.color}")

# Destructor

def __del__(self):

    print(f"Destructor called, {self.name} deleted.")

# Object creation

apple = Fruit('Apple', 'Red')

# Accessing object attribute

print(apple.name)

# Deleting object manually

del apple