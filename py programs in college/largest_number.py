# biggest number finding and it's position also

list_num =[]
n = int(input('How many numbers you want to input?\n'))

for i in range(n):
    '''
    creating list using user input
    '''
    i = int(input('Enter a number: '))
    list_num.append(i)
largest = list_num[0]
for i in range(n):
    '''
    finding the largest number
    '''
    if largest < list_num[i]:
        largest = list_num[i]
print('\n\nlargest number is',largest)
for i in range(n):
    '''
    position of largest number
    '''
    if largest == list_num[i]:
        print('The largest number is in ',i+1,' no position.')