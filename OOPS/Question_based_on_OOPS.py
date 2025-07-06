# Question 1: Class for complex number
"""
Create a python class named 'ComplexNumber' to represent complex numbers.

"""
class ComplexNumber:
    def __init__(self, real=0.0, imag=0.0):
        self.imag = imag
        self.real = real
    def conjugate(self):
        imag=self.imag* - 1
        print(f"({self.real} + {self.imag})")
cn1=ComplexNumber(3,5)
print(cn1.real)
print(cn1.conjugate())