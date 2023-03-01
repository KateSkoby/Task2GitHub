from random import randint

array = []

def createArray(number):
    array = [randint(5, number*100) for i in range(0, number+10)]
    print(array)

createArray(19)
