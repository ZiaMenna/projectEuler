#WIP

"""
Problem:
Let fn(k) = e^(k/n) - 1, for all non-negative integers k.

Remarkably, f200(6) + f200(75) + f200(89) + f200(226) = 3.141592644529… ≈ π.

In fact, it is the best approximation of π of the form fn(a) + fn(b) + fn(c) + fn(d) for n = 200.

Let g(n) = a2 + b2 + c2 + d 2 for a, b, c, d that minimize the error: | fn(a) + fn(b) + fn(c) + fn(d) - π|
(where |x| denotes the absolute value of x).

You are given g(200) = 62 + 752 + 892 + 2262 = 64658.

Find g(10000).
"""
"""
so pi ~= e^(6/200) + e^(75/200) + e^(89/200)+ e^(226/200) - 4
x = log(e^(3/100) + e^(3/8) + e^(89/200) + e^(113/100)) + 2 i π n and n element Z
so e^x = e^(3/100) + e^(3/8) + e^(89/200) + e^(113/100) 
x = 1.965935810935287648381271416376250141723438298917692127802 ... + 2 i π n and n element Z
s = (6+75+89+226)/200 = 1.98 is very close to x, but unrelated I fear

"""
