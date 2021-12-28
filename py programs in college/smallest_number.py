listt = []
n = int(input('How many numbers you want to check?\n'))
for i in range(n):
    i = int(input('Enter your number: '))
    listt.append(i)
smallest = listt[0]

for i in range(n):
    if smallest>listt[i]:
        smallest = listt[i]
print('Smallest number is ',smallest)

for i in range(n):
    if smallest == listt[i]:
        print('Smallest number is in ',i+1,'no position.')