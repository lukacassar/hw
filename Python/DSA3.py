import random
arr = []
eArr = [] # holds the extreme points
for i in range(10):
    arr.append(random.randint(0,20))
print(f"Unchecked array: {arr}")

def extremeCheck(arr):
    global epts
    epts = False
    for i in range(1, len(arr) - 1):
        if (arr[i] < arr[i-1] and arr[i] < arr[i+1]) or (arr[i] > arr[i-1] and arr[i] > arr[i+1]):
            eArr.append(arr[i])
            print(f"Value at index {i}: {arr[i]} is an extreme point")
            epts = True
        
    

extremeCheck(arr)
if epts:
    print(f"Line print of extreme points: {eArr}")
else:
    print("SORTED")

