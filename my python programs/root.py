# num = int(input('Enter: '))
# def root(x):
x = int(input('Enter a number: '))
x = float(x)
a = 0
while a**2 < x:
    a = a + 0.001
if a**2 == x:
    print('Square root of ', x,' is ',a)
else:
    print(a)