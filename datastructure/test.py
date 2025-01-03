import random
a=[random.randint(1,100) for i in range(10)]
print("排序前的数组:")
print(a)
print("排序后的数组:")
print(sorted(a))

m={"aa":12,"bb":2,"cc":34,"dd":14,"ee":65}
print(m)
print("按照值排序的字典:")
print(sorted(m,key=lambda x: m[x]))
