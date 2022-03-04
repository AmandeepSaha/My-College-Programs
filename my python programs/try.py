# listt = ['aman', 'isha','arman','debasish']
# def f(*names):
#     i=0
#     print('Hello ', end='')
#     while len(names) > i:
#         print(names[i],end=", ")
#         i += 1
# f('Aman', 'Isha', 'Arman', 'Debasish')

def greek(addresss='sir ',*name):
    print('Hello!',addresss,*name)
greek(addresss='sir','Elon Musk')