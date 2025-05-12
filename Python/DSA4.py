import random
arr = []
N = 50
for i in range(N):
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

found = False

for key in combinations.keys():
    ptr = combinations.get(key)
    if len(ptr) == 2:
        found = True
        print(f"Product {key} has combinations: {ptr}")
    elif len(ptr) > 2:
        found = True
        print(f"Product {key} has the following combinations")
        for i in range(len(ptr)):
            for j in range(i+1, len(ptr)):
                a = ptr[i]
                b = ptr[j]
                print(f"{a} and {b}")

if not found:
    print("There are no 2-pairs of integers having the same product for this run. Try increasing the value of N or re-run the code!")

""" rows = [f"Key {k} has value {v}" for k, v in combinations.items()]
max_len = max(len(row) for row in rows)

count = 0
print("FULL DICTIONARY:")
for k,v in combinations.items():
    text = f"Key {k} has value {v}"
    print(f"{text:<{max_len}}", end="\t")
    count += 1
    if (count == 5):
        count = 0
        print() """


