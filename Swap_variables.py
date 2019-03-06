# In this example, you will learn to swap two variables by using a temporary variable and, without using temporary variable.

a = 5
b = 6

print(f"Before swap: {a,b}")

temp = a
a = b
b = temp

print(f"After swap: {a,b}")

# Without using a temp variable
c = 8
d = 9

print(f"Before swap: {c,d}")

c, d = d, c

print(f"After swap: {c,d}")

e = 1
f = 2

print(f"Before swap: {e,f}")

e = e + f
f = e - f
e = e - f

print(f"After swap: {e,f}")

g = 11
h = 12

print(f"Before swap: {g,h}")

g = g * h
h = g / h
g = g / h

print(f"After swap: {g,h}")

m = 15
n = 19

print(f"Before swap: {m,n}")

m = m ^ n
n = m ^ n
m = m ^ n

print(f"After swap: {m,n}")
