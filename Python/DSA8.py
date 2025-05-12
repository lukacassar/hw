def nrmethod(num):
    if num < 0:
        print("Cannot compute square root of a negative number")
    if num == 0:
        return 0
    
    x_0 = num / 2
