"""
Problem:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
"""
Procedure:
I can proceed with brutal calculations done by the computer or using tha Gauss formula for finding the sum of consecutive integers
i.e.: the sum of the first n natual numbers\{0} is n*(n+1)/2
If i consider only the first n numbers that are multiple of k : nk*(nk+1)/2, or k(n*(n+1)/2)
How much multiples of k there are in the first l natural numebrs\{0}? Well, there are floor(l/k).
So the sum of the numbers that are multiple of k and smaller or equal to l is: 
There is a simple caveat prior to applying this formula to 3 and 5 and summing all up: numbers multiple of 15 (3*5) are counted two times, so they must be subtracted one time from the total.

The advantage of this calculation is that it can be done by hand and is O(1). The iterative version is extremely shorter and is O(n).
"""
def getResultByCalculation():
    def gaussSum (n):
        """returns the sum of the first n natural numbers\{0}"""
        return int(n*(n+1)/2)

    limit = 1000 - 1             # numbers below 1000
    mult_3 = int(limit/3)        # number of multiples of 3, 5, 15 below or equal to l
    mult_5 = int(limit/5)
    mult_15 = int(limit/15)



    return 3 * gaussSum(mult_3) + 5 * gaussSum(mult_5) - 15 * gaussSum(mult_15) 
    # Subtracting the multiples of 15 because they are counted two times: as multiple of 3 and 5
    
    
def getResultByIteration():
    return sum(multiple for multiple in range(0, 1000) if ( multiple % 3 == 0 or multiple % 5 == 0))
    
def getResultByIteration_noHardcodedNumbers(limit, multiples):
    return sum(number for number in range(limit + 1) if any(number % mult == 0 for mult in multiples))
