# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n-1)


# n = int(input())
# print("This is factorial== ",fact(n))

# def sum(a):
#     result = 0
#     i=0
#     result = a[i]+result
#     i= i+1
#     subAr = a[:1]
#     if len(a)>=i:
#         sum(subAr)


# a = {1, 2, 3, 4, 5, 6}
# sum(a)


# a = "hemant"
# print(list(a))
# print(tuple(a))
# print(set(a))

# a= 1,2,4,5,8
# print(type(a))
# s= list(a)
# print(type(s))
# s.append(2)
# print(list(s))
# a=tuple(s)
# print(a)
# print(type(a))

# a =20
# print(bin(a))
# print(hex(a))
# print(oct(a))

# import math
# print(factorial(a))

# print("hemant","raj", end = " ")
# print("rahul", "raj",sep="//")
# print(end=" ")

# first_term= int(input("Enter the first term : "))
# common_term= int(input("Enter the common term : "))
# nth_term= int(input("Enter the nth term : "))

# power = first_term*common_term**(nth_term-1)
# print()
# print("this is your result",power)


# username = input("Choose a username: ")
# final_username = username.replace("-", ",")

# print("Your username is: " + final_username)


# dob1= input()
# dob2 = input()

# print(dob1.split("-"))

# a = [input(), tuple(map(int, input().split("-")))]
# b = [input(), tuple(map(int, input().split("-")))]

# if a[1] < b[1]:
#     print(a[0])
# elif a[1] > b[1]:
#     print(b[0])
# else:
#     if a[0] < b[0]:
#         print(a[0])
#     else:
#         print(b[0])

# import datetime
# name1= input()
# dob1 = input()
# name2= input()
# dob2 = input()

# dob1 = [int(x) for x in dob1.split("-")]
# dob2 = [int(x) for x in dob2.split("-")]

# print(dob1,dob2)

# if dob1 < dob2:
#     print(name1)
# elif dob1 > dob2:
#     print(name2)
# else:
#     print(name1 if name1 < name2 else name2)


# r = range(10)
# print(r)
# print(type(r))
# l = list(r)
# print(l)

# z = int(input("Enter the num whose table you wants : "))
# print()
# x = 1
# for i in range(z, 10*z+1, z):
#     print(x, "x", z, ":", end=" ")
#     x += 1
#     print(i)

# x = int(input("Enter num : "))
# for i in range(2,x+1):
#     if x%i==0:
#         print(i)
#         break


# x= int(input("enter the value of num : "))
# print()
# for i in range(1,11):
#     print(i, " : ",end ="")
#     for x in range(i,i*10+1,i):
#         print(x,end=" ")
#     print()

# for i in range(4):     #it is use for line change
#     for x in range(5):  #it is use for printing
#         print("*",end=" ")
#     print()



# y=20
# for i in range(y):
#     for x in range(y-i):
#         print(" ",end="")
#     for x in range(i):
#         print("","*",end="")
#     print()


# x= int(input("Enter the number : "))
# count =0
# while x!=0:
#     x= x//10
#     count +=1
# print(count)


# gcd 

# x,y= int(input()),int(input())
# for i in range(2,(x and y)+1):
#     if x%i==0 and y%i==0:
#         print(i)


# lcm

# x,y = int(input()),int(input())
# res = max(x,y)
# while res <=x*y:
#     if res%x==0 and res%y==0:
#         break
#     res+=1
# print(res)


# x = int(input())
# if x ==0:
#     print(1)
# elif x==1:
#     print(1,1)
# else:
#     print(1,1,end=" ")
#     a=1
#     b=1
#     for i in range(2,x):
#        c=a+b
#        print(c,end=" ")
#        a=b
#        b=c










# num = int(input("enter the number : "))
# if num==0:
#     print(1)
# elif num==1:
#     print(1,1)
# else:
#     print(1,1,end=" ")
#     a=1
#     b=1
#     for i in range(2,num):
#        c=a+b
#        print (c,end=" ")
#        a=b
#        b=c





# num = int(input("enter the number : "))
# count = 0
# for i in range(1,num+1):
#     if num%i==0:
#         count +=1
# if count<3:
#     print(num," is prime number")
# else:
#     print("its not a prime number ")

# print(count)




num = int(input("Enter :"))
x= 1
while x*x<num:
    if num%x==0:
        print(x)
        print(num//x)
    x+=1
if x*x==num:
    print(x)

