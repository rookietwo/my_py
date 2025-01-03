str1 = "Hello Python"
str2 = ","
for m in str1:
    print(m, end="")
print()
print(str1[::2])
print(str1[1::2])
print(str1[::-1])
print(str1.isalnum())
print(str1.split())
a = ['a', 'b', 'c']
print(str2.join(a))

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
result = x.intersection(y, z)
print(result)
