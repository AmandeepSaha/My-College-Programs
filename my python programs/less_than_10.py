# This programs prints all less numbers than 10, is provided by users

listt_of_num=[]
new_listt=[]
your_numb = int(input('You want add numbers:\n'))

for i in range(your_numb):
    i = int(input('Enter your number: '))
    listt_of_num.append(i)
print('You have entered the numbers ',listt_of_num)

