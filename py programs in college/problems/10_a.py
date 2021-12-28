# Question no 10.a
# College paper
# 28/12/21
# Question: Write a program to compute sum of 1st n natural numbers

n = int(input('n = '))
tuplee = []

for i in range(1,n+1):
    tuplee.append(i)
# print section
print('Sum of 1st n-th natural numbers is ', sum(tuplee))