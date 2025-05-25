def maclaurin(ang, n, trig):
    if n < 1:
        return "Number of terms must be at least 1"
    if trig not in ['sin', 'cos']:
        return "Trig function must be 'sin' or 'cos'"
    
    finalAns = 0
    if trig == 'sin': # the first terms
        ans = ang
    else:
        ans = 1
    
    for r in range(0,n):
        finalAns += ans
        if trig == 'sin':
            ans *= -(ang * ang) / ((2 * r + 2) * (2 * r + 3)) # Writing the series as a simple product to avoid large factorials. Divide the (k+1)th term by the kth term to get this expression.
        else:
            ans *= -(ang * ang) / ((2 * r + 1) * (2 * r + 2)) # Same, but slightly different for cos.
    return finalAns


trig = input("Choose sin or cos ")
ang = float(input("What angle? (Radians) "))
n = int(input("How many terms to calculate Maclaurin Series? "))

print(f"Maclaurin series answer: {maclaurin(ang,n,trig)}")
    
    
    