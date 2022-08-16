from operator import truediv


xs = [()]

print(xs)

res = [False] * 2

print(res)

if xs:
    res[0] = True 

print(res)

if xs[0]:
    res[1] = True

print(res)

#Special COnditional
a = True
b = True

#a == not b
not a == b
not (a == b)
a == (not b)

def division(x,y):
    return x // y

division(5,10)
