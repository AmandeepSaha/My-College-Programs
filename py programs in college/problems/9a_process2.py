# Question no 9.a
# College paper
# 28/12/21
# Question: Write a program to compute sum of all odd numbers from 1st n natural numbers

n = int(input('n = '))
adding_list = []
for i in range(1,n+1):
    if i%2==0:
        pass
    else:
        adding_list.append(i)

print('Sum of first ',n,' th ','odd natural numbers is ',sum(adding_list))