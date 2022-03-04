# x**2 - 4x - 10 = 0

# num = int(input('Enter: '))
def root(x):
    # x = int(input('Enter a1 number: '))
    # x = float(x)
    a1 = 0
    while a1**2 < x:
        a1 = a1 + 1
    if a1**2 == x:
        print('Square root of ', x, ' is ', a1)
    else:
        print(a1)

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

# import root
# a*x**2 + b*x - c == 0

root_var = b**2-4*a*c
x1 = -b/2*a + root(root_var)/2*a

print(x1)