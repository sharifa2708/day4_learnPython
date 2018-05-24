t = 12345, 54321, 'hello!'
print(t[0])

print(t)

u = t, (1, 2, 3, 4, 5)
print(u)

# Tuples are immutable:
# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print(v)

