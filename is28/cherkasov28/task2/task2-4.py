import random

def isIncreasingSequence(arr):
    for i in range(0,len(arr)-1):
        if(arr[i] >= arr[i+1]):
            return False
    return True


a = [random.random() for i in range(0,10)]

print("Массив: ",a,"\nЭто возрастающая последовательность: ",isIncreasingSequence(a))