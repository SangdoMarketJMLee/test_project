class CalculatorSuper:
    def add(self,n1,n2):
        return n1 + n2
    def sub(self,n1,n2):
        return n1 - n2

class CalculatorChild(CalculatorSuper):
    def mul(self,n1,n2):
        return n1 * n2
    def div(self,n1,n2):
        return n1 / n2
myCalculator = CalculatorChild()

print(myCalculator.add(10,20))
print(myCalculator.sub(10,20))
print(myCalculator.mul(10,20))
print(myCalculator.div(10,20))