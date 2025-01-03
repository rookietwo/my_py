# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d x %d = %d" % (i,j,i*j),end="\t")
#     print("\n")

# sum = 0
# for i in range(1,101):
#     if i%2 != 0:
#         sum = sum + i
# print(sum)

# a = int(input("输入一个整数"))
# sum = 0
# b = 2 ** 64 - 1
# if (a > 0):
#     for i in bin(a)[2:]:
#         if i == '1':
#             sum += 1
# else:
#     for i in bin(a & b)[2:]:
#         if i == '1':
#             sum += 1
# print("整数%d的二进制表示中1的个数为%d" % (a, sum))

a = [8, 2, 3, 4, 5, 6, 7, 1, 9, 10]
print(sorted(a))

b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
c = [j for i in b for j in i]
print(c)
