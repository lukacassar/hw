def nrmethod(num, tolerance, maxIterations):
    if num < 0:
        print("Cannot compute square root of a negative number")
    if num == 0:
        return 0
    
    x_0 = num / 2

    for i in range(maxIterations):
            x_1 = (x_0 + num / x_0) / 2
            if abs(x_0 * x_0 - num) < tolerance:
                return x_1
            x_0 = x_1
    print("MAX ITERATIONS")
    return x_0
    
num = float(input("Enter a number "))
tolerance = float(input("Enter tolerance "))
maxIterations = int(input("Enter max iterations "))

result = nrmethod(num, tolerance, maxIterations)
print(f"Approximate square root is {result:.6f}")