def isPrime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
        
def sieve(num):
    prime = [True for i in range(num+1)]
    prime[0] = prime[1] = False

    for i in range(2, num + 1):
        if prime[i]:
            for j in range(i * 2, num + 1, i):
                prime[j] = False

    for i in range(2, num+1):
        if prime[i]:
            print(i, end= " ")        
        



try:
    num = int(input("Enter a whole number to check if it's prime \n"))
    print(isPrime(num))
except ValueError:
    print("You did not input a whole number. Program will now terminate.")
    exit(1)

try:
    num = int(input("Enter a whole number to perform Sieve of Eratosthenes on. \n"))
    sieve(num)
except ValueError:
    print("You did not input a whole number. Program will now terminate.")
    exit(1)




