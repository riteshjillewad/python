a = 100
b = 200

print("Before modification: ")
print("a: {a}, memory:",id(a))
print("b: {b}, memory:",id(b))

# If we change the values, new memory will be allocated as integer objects are immutable

a = 500
b = 600

print("After modification: ")
print("a: {a}, memory:",id(a))
print("b: {b}, memory:",id(b))