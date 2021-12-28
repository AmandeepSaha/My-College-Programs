# Question no 9.a
# College paper
# 28/12/21
# Question: Write a program to compute sum of all odd numbers from 1st n natural numbers

n = int(input('n = '))
addin_list = []
a = 1

for i in range(1,n+1):
    if a%2==0:
        pass
    else:
        addin_list.append(a)
    a+=1
    
# print section
print('Sum of all odd numbers from 1st ',n,' natural numbers is ', sum(addin_list))