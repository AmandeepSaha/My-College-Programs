# This is a calculator, made by me which will come in handy

functionns = input('Hey! I\'m a calculator. I\'ll help you in \n(i) Addition\n(ii) Subtraction\n(iii) Multiplication\n(iv) Division\n\nPress\n\t\'+\' for Addition\n\t\'-\' for Subtraction\n\t\'*\' for Multiplication\n\t\'/\' for Division\n\n\t\t')


if functionns == '+':
    n_add=int(input('You want to add _____ number/numbers: '))
    listt_add = []
    for item_add in range(n_add):
        item_add = int(input('Enter number: '))
        listt_add.append(item_add)
    after_addition = sum(listt_add)
    print('The sum of your provided numbers is',after_addition)
elif functionns == '-':
    a = int(input('Enter your 1st number: '))
    b = int(input('Enter your 2nd number: '))
    print('Subtraction of',a,' and ',b,' is ',a-b)
    you_want_to_sub_more = input('Do you want to subtract more? Press \'y\' for \'yes\' and \'n\' for \'no\'\n\n\t')
    while you_want_to_sub_more == 'y':
        a=int(input('\nEnter your 1st number: '))
        b=int(input('Enter your 2nd number: '))
        print('Subtraction of', a, ' and ', b, ' is ', a-b)
elif functionns == '*':
    a_mul = int(input('Enter your 1st number: '))
    b_mul = int(input('Enter your 2nd number: '))
    print('Multiplication of ',a_mul,' and ',b_mul,' is ',a_mul*b_mul)
    you_want_to_mul_more = input('Do you want to subtract more? Press \'y\' for \'yes\' and \'n\' for \'no\'\n\n\t')
    while you_want_to_mul_more == 'y':
        a_mul = int(input('Enter your 1st number: '))
        b_mul = int(input('Enter your 2nd number: '))
        print('Multiplication of ', a_mul, ' and ', b_mul, ' is ', a_mul*b_mul)
else:
    a_div = int(input('Enter divident: '))
    b_div = int(input('Enter divisor: '))
    print('Integral part ',a_div//b_div,' and factorial part is ',a_div%b_div)