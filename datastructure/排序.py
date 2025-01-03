# 学生 屠浩天
# 2025年01月02日14时26分59秒
import random


class Sort:
    def __init__(self, n):
        self.length = n
        self.arr = [random.randint(0, 100) for i in range(n)]

    def partition(self, left, right):
        arr = self.arr
        k=left
        for i in range(left, right):
            if arr[i] < arr[right]:
                arr[i], arr[k] = arr[k], arr[i]
                k += 1
        arr[k], arr[right] = arr[right], arr[k]
        return k

    def quicksort(self, left, right):
        if left < right:
            pivot = self.partition(left, right)
            self.quicksort(left, pivot - 1)
            self.quicksort(pivot + 1, right)

a=Sort(10)
a.quicksort(0,9)
print(a.arr)