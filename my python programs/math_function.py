a = int(input('Enter a number: '))
n = 1000000
listt=[]

for i in range(1,n+1):
    term = 1/a**i
    listt.append(term)
x=sum(listt)
print(x)