a = [0, 1, 2]
b = a
print a,b
c = a[:]

b[0] = "hello"

print a,b

c.append(3)

print c,b
