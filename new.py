print("hello world")

x=5
y=1.0
z=1j
print(type(x))
print(type(y))
print(type(z))

x=float(1)
y=int(2.8)
z=complex(3)
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))

a="hello world"
print(a[2:9])

a="hello world"
print(len(a))

for x in "banana":
    print(x)

txt="the best things in life are free"
print(" not free"in txt)
print("free"in txt)
print("tree"not in txt)

a="     hello world         "
print(a.strip())

a="hello world"
print(a.replace("h","j"))

a="hello ,world"
print(a.split(","))

a="hello"
b="world"
c=a + b
print(c)
