import random

arrA = []
sizeA = 300
arrB = []
sizeB = 400

for size in range(sizeA):
    arrA.append(random.randint(0,1024))

for size in range(sizeB):
    arrB.append(random.randint(0,1024))

temp = 0

print(f"Unsorted Array A: {arrA}")
print(f"Unsorted Array B: {arrB}")

# Shell Sort
gap = sizeA // 2
flag = True
while gap >= 1 and flag == True:
    flag = False
    for i in range(sizeA - gap):
        if arrA[i] > arrA[i + gap]:
            temp = arrA[i]
            arrA[i] = arrA[i + gap]
            arrA[i + gap] = temp
            flag = True
    if gap > 1:
        gap = gap // 2

# Quick Sort
def qSort(arr):
    quick(arr, 0, len(arr) - 1)

def quick(arr, first, last):
    if first < last:
        pivotPos = partition(arr, first, last)
        quick(arr, first, pivotPos - 1)
        quick(arr, pivotPos + 1, last)

def partition(arr, first, last):
    pivot = arr[first]
    u = first
    d = last
    while True:
        while u < last and arr[u] <= pivot:
            u += 1
        while arr[d] > pivot:
            d -= 1
        if u < d:
            temp = arr[u]
            arr[u] = arr[d]
            arr[d] = temp
        else:
            break
    temp = arr[first]
    arr[first] = arr[d]
    arr[d] = temp
    return d

qSort(arrB)

print(f"Sorted Array A: {arrA}")
print(f"Sorted Array B: {arrB}")

arrC = []

ptr1 = 0
ptr2 = 0

while ptr1 < sizeA and ptr2 < sizeB:
    if arrA[ptr1] > arrB[ptr2]:
        arrC.append(arrB[ptr2])
        ptr2 += 1
    elif arrB[ptr2] > arrA[ptr1]:
        arrC.append(arrA[ptr1])
        ptr1 += 1
    else:
        arrC.append(arrA[ptr1])
        arrC.append(arrB[ptr2])
        ptr1 += 1
        ptr2 += 1

while ptr1 < sizeA:
    arrC.append(arrA[ptr1])
    ptr1 += 1

while ptr2 < sizeB:
    arrC.append(arrB[ptr2])
    ptr2 += 1

print(f"Merged Array: {arrC}")

print(f"Size of Array A is {len(arrA)}, B is {len(arrB)} and C is {len(arrC)} ")




        