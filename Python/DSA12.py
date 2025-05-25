def sumFibonacci(n):
        
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    a = 1
    b = 1
    total = 2  # Sum of first two terms
    
    for i in range(3, n + 1):
        c = a + b
        total += c  
        a = b
        b = c
    
    return total

n = int(input("How many fibonacci terms? "))
print(f"Sum of the first {n} terms is {sumFibonacci(n)}")