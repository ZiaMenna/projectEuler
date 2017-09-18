from sympy.ntheory import isprime
from sympy import nextprime, primerange
for num1 in primerange(1000, 10000):
    num2 = num1
    num3 = num1
    while num3 < 10000:
        num2 = nextprime(num2)
        num3 = num2 + ( num2 - num1)
        if isprime(num3):
			if sorted(str(num1))==sorted(str(num2))==sorted(str(num3)):
            print(str(num1)+str(num2)+str(num3))
