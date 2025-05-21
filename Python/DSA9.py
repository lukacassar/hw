def findRepeated(arr):
    freq = {}
    nums = []
    for i in arr:
        if (freq.get(i) is not None):
            freq[i] = freq[i] + 1
        else:
            freq[i] = 1
            
    for i in freq.keys():
        if freq.get(i) > 1:
            nums.append(i)
    return nums

arr = [1,2,1,5,6,5,8,9,56,4,2,5,7,3,2,1,4]
result = findRepeated(arr)
if len(result) != 0:
    print(f"Numbers repeated more than once: {result}")
else:
    print("No numbers are repeated more than once")