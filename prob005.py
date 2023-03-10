'''
Sum square difference
Submit

 Show HTML problem content 
Problem 6
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 
.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
sum_sq = 0
for i in range (1,101):
    sq = i ** 2
    sum_sq = sum_sq+ sq
    
sq_sum = 0
s = 0 
for i in range(1,101):
    s = s + i
sq_sum = s ** 2
dif = sq_sum - sum_sq
print(dif)
