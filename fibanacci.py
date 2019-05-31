nterms = int (input("Enter the number of terms: "))

fib0 = 0
fib1 = 1
count = 0

if (nterms < 0):
    print ("Provide a valid input")
elif (nterms == 1):
    print (f"The Fibonacci series is {fib0}")
else:
    print ("The fibonacci series is: \n")
    while(count < nterms):
        print (fib0, end=' , ')
        n = fib0 + fib1
        fib0 = fib1
        fib1 = n
        count += 1
