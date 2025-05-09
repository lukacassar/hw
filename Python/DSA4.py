import random
arr = []
for i in range(50):
    arr.append(random.randint(1,1024))

combinations = {}

# Storing ALL UNIQUE COMBINATIONS as dictionary with array values
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        a = arr[i]
        b = arr[j]
        product = a*b

        if product not in combinations.keys():
            combinations[product] = []
        if a>b: # Storing as a sorted tuple to avoid duplicates, easier to work with also.
            a,b = b,a
        if (a,b) not in combinations[product]:
            combinations[product].append((a,b))


for key in combinations.keys():
    ptr = combinations.get(key)
    if len(ptr) == 2:
        print(f"Product {key} has combinations: {ptr}")
    elif len(ptr) > 2:
        print(f"Product {key} has the following combinations")
        for i in range(len(ptr)):
            for j in range(i+1, len(ptr)):
                a = ptr[i]
                b = ptr[j]
                print(f"{a} and {b}")
                
                

