# Custom self made key parameter

def myfunc(n):
  return abs(n)

a = (5.1, 3.112, 1, 11, 2, 12, 17)
x = sorted(a, key=myfunc)
print(x)