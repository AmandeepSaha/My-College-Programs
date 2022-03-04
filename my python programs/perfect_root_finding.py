# import math as m
# def f():
#     x = x1 + y1

def f_Root(x):
    """
    this programme will calculate root of a quadratic eqn
    """
    y = f_Root(x)
    x1 = f_Root(x) + 1
    y1 = f_Root(x1)
    while y != 0:
        '''
        iteration over periode
        '''
        dellx = x1 - x
        m = y1/dellx
        x = x1 + y1/m
    if y == 0:
        print(x)