def findLargest(arr):
    if len(arr) == 0:
        return("None, since the list is empty.")
    if len(arr) == 1:
        return arr[0]
    tail = findLargest(arr[1:])
    if arr[0] > tail:
        return arr[0]
    else:
        return tail
    

arr = []
print(f"Largest number: {findLargest(arr)}")