class expression:
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value
class addition(expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate()
class multiplication(expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self):
        return self.left.evaluate() * self.right.evaluate()
expr1 = addition(expression(5), expression(3)) 
expr2 = multiplication(expression(2), expression(4))  
expr3 = addition(expr1, expr2)  # Represents 
print(expr3.evaluate())  
