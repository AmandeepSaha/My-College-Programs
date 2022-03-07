# write a program to print all prime number list up to a particular number

you_num = int(input('Enter a number:\t'))
l_i = []
total_count =[]
counting_num = 1
while counting_num<=you_num:
    for i in range(1,you_num+1):
        if counting_num%i == 0:
            l_i.append(i)
    if l_i == [1,you_num]:
        total_count.append(counting_num)
    print(total_count)
    counting_num += 1