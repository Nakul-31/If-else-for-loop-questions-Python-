#Question 1
print("\nQus-1")

#WAP Ask user to input a number and then month name corresponding to that number

#months
months = ["Jan", "Feb", "March", "April", "May", "June","July", "Aug", "Sept", "Oct", "Nov", "Dec"]

num = int(input("enter a no. between 1 to 12: "))

if 1 <= num <= 12:
   
    for i in range(1, 13):
        if num == i:
            print(f"The month is {months[i - 1]}")
else:
    print("Invalid number! enter a no. bteween 1 to 12")

print("\n-------------------")
print("\n-------------------")

#Question 2:
print("\nQus-2")


num1 = int(input("enter the first no.: "))
num2 = int(input("enter the second no.: "))
print("\n-------------------")


if num1 == num2:
    print("both no. are equal.")
else:
    print("the no. are not equal.")
print("\n-------------------")



if num1 > num2:
    print("the first mo. is bigger.")
elif num2 > num1:
    print("the second no. is bigger.")
print("\n-------------------")



if num1 <= num2:
    print("the first no. is smaller than or equal to the second no.")
else:
    print("the first number is greater than the second no.")
print("\n-------------------")


if num1 > num2:
    print("first no. is greater than second, printing your first name 5 times:")
    for i in range(5):
        print("Nakul")
elif num1 < num2:
    print("first no. is less than second, printing your surname 3 times:")
    for i in range(3):
        print("Dhiman")
print("\n-------------------")
print("\n-------------------")

#Question 3:
print("\nQus-3")

string1 = input("first string: ")
string2 = input("second string: ")


if string1 == string2:
    print("strings are equal")
else:
    print("strings are NOT equal")


if string1 is string2:
    print("both strings are the same")
else:
    print("both strings are NOT the same")    


print("\n-------------------")
print("\n-------------------")
#Question 4:
print("\nQus-4")

str1 = input("enter firsst string: ")
str2 = input("enter secound string): ")


num1 = int(str1)
num2 = int(str2)


if num1 is num2:
    print(" the no. are in the same memory")
else:
    print("the no. are NOT in the same memory")


print("\n-------------------")
print("\n-------------------")

#Question 5:
print("\nQus-5")

a = int(input("enter a no.: "))

total = 0

for i in range(1, a + 1):
    total += i

print("The sum of numbers from 1 to", a, "is:", total)

print("\n-------------------")
print("\n-------------------")

#Question 6:

print("\nQus-6")
num = int(input("input no.: "))

print("even no. are:")

for i in range(2, num, 2):
    print(i, end=",")


#Question 7:
print("\n-------------------")
print("\n-------------------")
print("\nQus-7")


num = int(input("enter a no: "))

op = input("enter OP (+ or -): ")

if op == '+':
    for i in range(num):
        print(i, end=", ")
elif op == '-':
    for i in range(num, 0, -1):
        print(i, end=", ")
else:
    print("invalid operator.please enter only + or -.")





#Question 8:
print("\n-------------------")
print("\n-------------------")
print("\nQus-8")

num = int(input("enter a no.: "))

print(f"table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")




#Question 9:
print("\n-------------------")
print("\n-------------------")
print("\nQus-9")

for i in range(1, 5):
    for j in range(1, i+1): 
        print(j, end=' ')
    print() 



#Question 10:
print("\n-------------------")
print("\n-------------------")
print("\nQus-10")

N = int(input("enter a no.: "))

for i in range(1, N + 1):
    print(f"square of {i} is {i ** 2}")

