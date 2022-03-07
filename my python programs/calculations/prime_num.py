# We'll be writing a program to check if a number is prime number or not

a = int(input('Enter a number:\t'))
i = 1
l = []
for i in range(1,a+1):
    rem = a%i
    if rem == 0:
        l.append(i)
    i += 1
if l == [1,a]:
    print('This is a prime number.')
else:
    print('This is not a prime number.')