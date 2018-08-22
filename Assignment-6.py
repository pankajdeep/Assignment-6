#Q.1- Create a function to calculate the area of a sphere by taking radius from user.
import math
def area_of_sphere(radius):
    area=4*(math.pi)*(radius**2)
    return area
r=int(input("Enter radius of sphere"))
print("Area of Sphere is :",area_of_sphere(r))


#Q.2- Write a function “perfect()” that determines if parameter number is a perfect number.
#Use this function in a program that determines and prints all the perfect numbers between 1 and 1000. 
#[An integer number is said to be “perfect number” if its factors, including 1(but not the number itself), sum to the number.
#E.g., 6 is a perfect number because 6=1+2+3].
def perfect(num):
        sums=0
        for j in range(1,num):
            if(num%j==0):
                sums=sums+j
        if(sums==num):
            print(num)
print("Perfect Numbers between 1 and 1000 are :")
for i in range(2,1000):
    perfect(i)


#Q.3- Print multiplication table of n using loops, where n is an integer and is taken as input from the user.
def multiply(num):
    for i in range(0,11):
        print(num,"*",i,"=",num*i)
num=int(input("Enter integer whose multiplication table you want to print"))
multiply(num)


#Q.4- Write a function to calculate power of a number raised to other ( a^b ) using recursion.
def power(a,b):
    if(b>1):
        return(a*power(a,b-1))
    elif(b==0):
        return 1
    else:
        return a
num1=int(input("Enter value of a"))
num2=int(input("Enter value of b"))
print(num1,"^",num2,"=",power(num1,num2))
