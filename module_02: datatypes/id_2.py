# Since both the variables hold the same value, new memory is not allocated, both the variables will point to same memory location

a = 10
b = a

print(id(a))
print(id(b))