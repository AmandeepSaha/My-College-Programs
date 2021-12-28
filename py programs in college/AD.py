programme = input('You want to arrange numbers in ascending order or descending order?\nType \'a\' for arranging numbers in ascending order and type \'d\' to arrange numbers in descending order\nType here: ')    

a = 'ascending order'
d = 'descending order'


if programme=='a':
    listt_num = []
    n = int(input('How many numbers want to arrange in ascending order?\n'))

    for i in range(1, n+1):
        '''
        enter the numbers, i'll append into list
        '''
        i = int(input('Enter your number: '))
        listt_num.append(i)
    # print(listt_num)

    for i in range(n):
        '''
        function: creates a list of numbers in ascending order which is given by the user.
        '''
        for j in range(i+1, n):
            if listt_num[i] < listt_num[j]:
                temp = listt_num[j]
                listt_num[j] = listt_num[i]
                listt_num[i] = temp
            else:
                pass
    print(listt_num)
elif programme == 'd':
    # This programme arranges the list of given numbers into descending order list.

    listt_num = []
    x = int(input('Enter the number you want to arrange into descending order:\n'))

    for i in range(x):
        '''
        creates a list of given using data of user
        '''
        i = int(input('Enter your number: '))
        listt_num.append(i)

    for i in range(x):
        '''
        function: creates a list of numbers in descending order which is given by the user.
        '''
        for j in range(i+1, x):
            if listt_num[i] > listt_num[j]:
                temp = listt_num[j]
                listt_num[j] = listt_num[i]
                listt_num[i] = temp
            else:
                pass
    print(listt_num)