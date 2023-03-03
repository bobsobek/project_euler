num = int(input("number:"))
low_lim = 1
upp_lim = num
factors = []
terminate = 0
a = 2
while not num == 1:
    if num%a == 0:
        factors.append(a)
        num = num/a
        a = 2
    a = a + 1
    
print(factors)
