"""
magic method 
they got called themself

"""
class ComplexNumber:
    def __init__(self,real=0.0,imag=0.0):
        self.imag = imag
        self.real = real

    def __str__(self): # magic method
        if(self.real==0):
            return f"{self.imag}i"
        elif(self.imag<0):
            s = f"{self.real}{self.imag}i"
        else:
            s = f"{self.real}+{self.imag}i"
        return s


    def __add__(self,other):
        resultReal =0
        resultImag = 0
        
        resultReal = self.real + other.real
        resultImag = self.imag + other.imag
        ans = ComplexNumber(resultReal,resultImag)

        return ans

    def __sub__(self,other):
        # print("I am here")
        resultReal =0
        resultImag = 0
        
        resultReal = self.real - other.real
        resultImag = self.imag - other.imag
        ans = ComplexNumber(resultReal,resultImag)
    
        return ans

    def __mul__(self,other):
        resultReal =0
        resultImag = 0
        
        resultReal = self.real * other.real - self.imag * other.imag
        resultImag = self.real * other.imag + other.real * self.imag
        ans = ComplexNumber(resultReal,resultImag)
    
        return ans

    def __truediv__(self,other):
        resultReal =0
        resultImag = 0
        den = other.real**2 + other.imag**2
        ans = self * ComplexNumber(other.real/den,(-1*other.imag)/den)
        return ans
    
    def conjugate(self):
        return ComplexNumber(self.real,-1*self.imag)

    def __eq__(self,other):
        return (self.real == other.real) and (self.imag == other.imag)

cn1=ComplexNumber(3,5)
print(cn1.conjugate())