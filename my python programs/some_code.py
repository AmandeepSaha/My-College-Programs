x = int(input('x = '))
n = 3
a = []
b = 1/x**2*n

# print(b)

while b > 0.0001:
    a.append(b)
    n+=1
print(a)
