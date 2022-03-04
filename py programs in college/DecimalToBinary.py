# Decimal to Binary number

num = int(input('Enter Your Decimal Number:\t'))

def decimalToBinary(x):
    '''
    This program converts decimal numbers into binary number
    '''
    if x > 1:
        decimalToBinary(x//2)
    print(x%2,end='')

decimalToBinary(num)