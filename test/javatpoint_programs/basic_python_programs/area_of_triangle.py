

a = int(input("enter 1st side : "))
b = int(input("enter 2nd side : "))
c = int(input("enter 3rd side : "))

# primeter of triangle
s = (a+b+c)/2

#area of triangle

area = (s*(s-a)*(s-b)*(s-c))**0.5
print("area of triangle = %.2f " % area)