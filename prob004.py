
"""
Largest palindrome product
Submit

 Show HTML problem content 
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
a = 999
b = 999
terminate = 0 
ans_l =[]
while terminate == 0:
    num = a * b
    num = str(num)
    num_l = list(num)
    c = 0
    false = 0
    while c < len(num_l)/2 :
        if num_l[c] != num_l[-c-1]:
            false = 1
        c = c+1
    if false == 0:
        ans_l.append(int(num))           
    a =a-1
    if a == 0:
        b = b - 1
        a = 999
    if b ==0:
        terminate = 1

ans_l.sort()
ans = ans_l[-1]
print(ans)
