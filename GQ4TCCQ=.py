#WIP
"""
Problem GQ4TCCQ= 

We call a positive integer double pandigital if it uses all the digits 0 to 9 exactly twice (with no leading zero). For example, 40561817703823564929 is one such number.
How many double pandigital numbers are divisible by 11?
"""

"""
Divisibilty rules for 11, according to wikipedia:
1- Form the alternating sum of the digits. The result must be divisible by 11.[1][4] 	
    918,082: 9 − 1 + 8 − 0 + 8 − 2 = 22 = 2 × 11.
2- Add the digits in blocks of two from right to left. The result must be divisible by 11.[1] 	
    627: 6 + 27 = 33 = 3 × 11.
3- Subtract the last digit from the rest. The result must be divisible by 11. 	
    627: 62 − 7 = 55 = 5 × 11.
4- Add the last digit to the hundredth place (add 10 times the last digit to the rest). The result must be divisible by 11. 	
    627: 62 + 70 = 132: 13 + 20 = 33 = 3 × 11.
5- If the number of digits is even, add the first and subtract the last digit from the rest. The result must be divisible by 11. 	
    918,082: the number of digits is even (6) → 1808 + 9 − 2 = 1815: 81 + 1 − 5 = 77 = 7 × 11
6- If the number of digits is odd, subtract the first and last digit from the rest. The result must be divisible by 11. 	
    14,179: the number of digits is odd (5) → 417 − 1 − 9 = 407 = 37 × 11
---
It looks like that rules from 3 to 6 are suitable for recursively reducing the 20! possible doubly pandigital numbers, for i can proceed by construction form the number 0

"""
from collections import deque
numberCache = deque(str(n) for n in range(10))
numberCache *= 2
# i must construct the number in this way: choose a digit divisible by 11 (0), use an inverse of a rule that subtracts two numbers, but instead add two suitable numbers
