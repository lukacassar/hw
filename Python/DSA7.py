import csv

def collatzSeq(num):
    seq = [num]
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = (3 * num) + 1
        seq.append(num)
    return seq



with open("collatz.csv", "w", newline='') as file:
    w = csv.writer(file)
    for i in range(2, 513):
        collatz = collatzSeq(i)
        # w.writerow(collatz) # Pure CSVs
        w.writerow([f"{i}: {','.join(map(str, collatz))}"]) # Prettier version
    print("collatz.csv was made in the same working directory as this project")
