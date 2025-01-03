# 学生 屠浩天
# 2025年01月02日20时28分17秒
import random
class Sort:
    def __init__(self, n):
        self.length = n
        self.arr = [random.randint(0, 100) for i in range(n)]
    def adjust_heap(arr, size, i):
        
