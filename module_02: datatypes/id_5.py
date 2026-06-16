# Mutable objects have different memory allocations

x = [1, 2, 3]
y = [1, 2, 3]

print(id(x))
print(id(y))