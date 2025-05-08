import random
arr = []
for i in range(10):
    arr.append(random.randint(0,20))

combinations = {}

# Storing ALL UNIQUE COMBINATIONS
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        a = arr[i]
        b = arr[j]
        product = a*b

        if product not in combinations.keys():
            combinations[product] = []
        combinations[product].append((a,b))

pairs = {}




