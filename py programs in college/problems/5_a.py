# college
# question: 5/a
# date: 22/12/21


x = int(input('x=? \n\t'))
listt = []

for i in range(101):
    '''
    func: this program claculates the deiscrete sumation of the function "n**2*x", where n bleongs to {0,100} and x is a user defined real number. 
    '''
    item = i**2*x
    listt.append(item)
print(sum(listt))