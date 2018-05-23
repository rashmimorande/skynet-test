
n = int(input("enter a no.: "))
count = 0
for i in range(1,n+1):
    if n % i == 0:
        count = count+1
if count == 2:
    print("{0} is prime no.".format(n))

else:
    print("{0} is not prime no.".format(n))
