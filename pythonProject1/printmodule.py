def printmodule1(num):
    for i in range(num):
        print("printmodule1 is called")


def printmodule2(num):
    for i in range(num):
        print("printmodule2 is called")


def printmodule3(num):
    for i in range(num):
        print("printmodule3 is called")


if __name__ == '__main__':
    printmodule1(1)
    printmodule2(2)
    printmodule3(3)
