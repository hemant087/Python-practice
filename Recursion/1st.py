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


# optimize solution ------------------------------------->

# num = int(input("Enter :"))
# x = 2
# while x*x < num:
#     if num % x == 0:
#         print(x)
#         print(num//x)
#     x += 1
# if x*x == num:
#     print(x)


# n = int(input("is it prime : "))
# x=2
# while x*x<=n:
#     if n %x ==0:
#         print("NO")
#         break
#     x+=1
# else:
#     print("YES")

# ----------------------------------------------


# def printf(**detail):
#     for d,v in detail.item():
#         print(f"{d}"is )


# --------------------------------------------------------------------------


# txt = input()
# last = len(txt)-1
# first = 0

# while last > first:
#     if txt[last] != txt[first]:
#         print("NO")
#         break
#     last = last-1
#     first += 1
# else:
#     print("YES")


# -------------------------------------------------

# txt = input("Enter the string : ")
# sub_string = input("Enter the sub string: ")

# if txt.find(sub_string):
#     print("you got it !")


# ----------------------------------------------------------------------------


# n = input()
# x = []
# while len(n)>0:
#     x.append(n[-1])
#     n=int(n)//10
#     n=str(n)
# print(x)

# --------------------------------------------------------------------------

# a = "hemant"
# x=""
# for i in range(len(a)):
#     if a[i]=="a":
#         continue
#     else:
#         x = x+ a[i]
# print("abc",x)

# ---------------------------------------------------

# sub = input()
# string = input()
# x=0
# new=""
# while x!=len(sub):
#     for i in range(len(string)):
#         if string[i]==sub[x]:
#             continue
#         else:
#            new=new+string[i]
# print(new)


# marks= int(input())
# option = int(input())
# correct_option= input()
# marked_option = input()
# correct =0
# for i in range(len(marked_option)):
#         if marked_option[i] in correct_option:
#             correct =correct+ (marks/((len(correct_option)+1)//correct_option))
#         else:
#             print("0.00")
#             break
# print(correct)

# def action(str):
#     mid=(len(str))//2
#     print(str[mid-2],end="")
#     print(str[mid-1],end="")
#     print(str[mid])


# str = input()
# if len(str)%2==0:
#     action(str)
# else:
#     str= str+"."
#     action(str)


# import numpy
# Arr = {12, 35, 1, 10, 34, 1}
# print(type(Arr))


#  # function to find all prime factors of n
# def prime_factors(n):
#     i = 2
#     factors = []
#     while i * i <= n:
#         if n % i:
#             i += 1
#         else:
#             n //= i
#             if i not in factors:
#                 factors.append(i)
#     if n > 1:
#         if i not in factors:
#                 factors.append(i)
#     return factors

# # take input from user
# n = int(input("Enter a positive integer greater than 1: "))

# # call prime_factors function and print the result
# print("Prime factors of", n, "are:", prime_factors(n))


# num = int(input())
# sum = 0

# for i in range(num+1):
#     sum = sum+i
# print(sum)


# for char in 'a1b2c3d4e5':
#     if char in 'abcde':
#         print('|', end = '') # there is no space between the quotes
#         continue
#     print(char, end = '')  # there is no space between the quotes
# print('|')

# string = input()
# low_str =string.lower()
# res = ''.join(sorted(low_str))
# print(str(res))


# n= int(input())
# n=5

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j, end=",")
#     print()


# w.a.p to sort the list without builded in function


# l = [4,54,65,77,687,9.445,6778,86,6,5645,6,345,345,52,4,35,46,57,7]
# li = []

# while len(l) > 0:
#     min_value = l[0]
#     for i in range(1, len(l)):
#         if l[i] < min_value:
#             min_value = l[i]
#     li.append(min_value)
#     l.remove(min_value)

# print(li)


# if len(li)%2==0:
#     median = li[(len(li)+2)//2]
# else:
#     median = li[(len(li)+1)//2]
# print(median)


# dot product of two list ----------------------------

# l1=[2,4,6,8]
# l2=[1,3,5,7]
# dot=[]
# product =0

# for i in range(len(l1)):
#     dot.append(l1[i]*l2[i])
#     product = product+dot[i]
# print(dot, product)


# play with matrix  ----------------------------------


# m1=[1,2,3]
# m2=[4,5,6]
# m3=[7,8,9]

# n1=[9,8,7]
# n2=[6,5,4]
# n3=[3,2,1]

# mn1=[m1,m2,m3]
# mn2=[n1,n2,n3]
# sum=[[0,0,0],[0,0,0],[0,0,0]]

# num = 3

# for i in range(num):
#     for j in range(num):
#         for k in range(num):
#             sum[i][j] =sum[i][j] + mn1[i][k]*mn2[k][j]

# # print(mn1)
# # print(mn2)
# print(sum)


# by taking input from user

# n = int(input())

# for i in range(n):

# x = 0
# b=200
# while True:
#     if x < 10:
#         x = int(input("enter : "))
#         continue
#     elif b < x < b + 2:
#         break


# # get the maximum
# def get_max(L):
#     maxi = L[0]
#     for x in L:
#         if x > maxi:
#             maxi = x
#     return maxi
# # get the minimum


# def get_min(L):
#     mini = L[0]
#     for x in L:
#         if x < mini:
#             mini = x
#     return mini
# # get the range


# def get_range(L):
#     maxi = get_max(L)
#     mini = get_min(L)
#     return maxi - mini


# def is_perfect(num):
#     # Factor sum
#     fsum = 0
#     for f in range(1, num):
#         if num % f == 0:
#             fsum += f
#     # fsum == num is a Boolean expression
#     # It will evaluate to True if num is a perfect number
#     # And False otherwise
#     return fsum == num


# print(is_perfect(int(input())))


# def distance(word_1, word_2):
#     # first condition
#     if len(word_1) != len(word_2):
#         return -1
#     letters = 'abcdefghijklmnopqrstuvwxyz'
#     size = len(word_1)
#     dist = 0
#     for i in range(size):
#         c1, c2 = word_1[i], word_2[i]
#     # distance between letters
#     d = abs(letters.index(c1) - letters.index(c2))
#     dist += d
#     return dist


# def is_magic(mat):
#     # first get the dimension of the matrix
#     m = len(mat)
#     # the sum of the two diagonals
#     d1sum, d2sum = 0, 0
#     # (i, i) goes from top-left -> bottom-right
#     # (i, m - i - 1) goes from top-right -> bottom-left
#     # note that a single loop is enough; no nesting required
#     for i in range(m):
#         d1sum += mat[i][i]
#         d2sum += mat[i][m - i - 1]
#     # if the two diagonal sums are unequal, we can return NO
# # unnecessary computation can be avoided
#     if not (d1sum == d2sum):
#         return 'NO'
#     # get row-sum and column-sum
#     for i in range(m):
#         rsum, csum = 0, 0
#         for j in range(m):
#             rsum += mat[i][j]
#             csum += mat[j][i]
#         if not (rsum == csum == d1sum):
#             return 'NO'
#     # if the code reaches this level
#     # then all requirements of a magic-square are satisfied
#     # so we can safely return YES
#     return 'YES'


# Refer PPAs to understand this function
# def get_column(mat, col):
#     col_list = []
#     m = len(mat)
#     for row in range(m):
#         col_list.append(mat[row][col])
#     return col_list
# # We make use of get_column
# # to get the ith column
# # this is made the ith row in the transpose


# def transpose(mat):
#     m, n = len(mat), len(mat[0])
#     mat_trans = []
#     for i in range(n):
#         mat_trans.append(get_column(mat, i))
#     return mat_trans


# def fact(n):
#     a=1
#     for i in range(1,n+1):
#         a=a*i
#         print(a)
#     return a


# print("This is your factorial :  ",fact(5))


# def first_three(L):
#     f,s,t=0,0,0
#     for i in L:
#         if i>f:
#            f=i
#            s=f
#            t=s
#     return [f,s,t]


# L=[1,2,3,4,5,6]
# first_three(L)


# -----------------------------------------------------------------


# num = input()
# count=0
# correct =""

# for i in num:
#     if i=="i":
#         correct = correct+"1"
#         count +=1
#     elif i =="o":
#         correct = correct+"0"
#         count +=1
#     else:
#         correct = correct+i


# x=2
# cfrac = x+(x+1/(x+1/(x+1/(x+1/(x+1/x)))))
# # cfrac =x+(1/x)
# print(cfrac)

# str = input()
# start = int(input())
# end = int(input())
# new = ""

# while len(new) < len(str):
#     for i in range(len(str)):
#         if start <= i and i <= end:
#             new+=str[i]

# print(new)


# m = int(input())
# n = int(input())

# if m < n:
#     print(m)
# else:
#     while m > n:
#         m -= n
#         # print(m)
#     print(m)


# num = []
# count = 0
# while count < 4:
#     num.append(int(input()))
#     count += 1
# num = sorted(num)
# print(num)
# print(" ".join(str(i) for i in num))


# x = []
# count=0
# while count<4:
#     x.append(int(input()))
#     count +=1
# x.sort()

# print(" ".join(str(i) for i in x))


# word = "edoucatinmoon"
# vowels = ['a', 'e', 'i', 'o', 'u']
# for v in vowels:
#     if v not in word:
#         print('not perfect')
#         break
# else:
#     vowel_count = [word.count(v) for v in vowels]
#     for i in range(len(vowels)):
#         for j in range(i+1,len(vowels)):
#             if word.find(vowels[i])>word.find(vowels[j]):
#                 print('not perfect')
#                 break
#             if vowel_count[i]<vowel_count[j]:
#                 print('not perfect')
#                 break
#         else:
#             continue
#         break
#     else:
#         print('perfect')


# (pas[0].isupper() or pas[0].islower())

# pas = input()
# spc = ['/', '\\', '=', "'", '"', ' ']
# if 8 >= len(pas) <= 32 or not(pas[0].isalpha()) or any(char in spc for char in pas) :
#     print('False')
# else:
#     print('True')


# str = input()

# vowel = ['a','e','i','o','u']

# for v in vowel:
#     if v not in str:
#         print("not perfect")
#         break
# else:
#     vowel_count =
#     for i in range(len(str))

# pas = input()
# valid = False
# if 8<=len(pas)<=32 and pas[0].isalpha():
#     if not('/'in pas or '\\'in pas or '='in pas or '"'in pas or "'"in pas or " "in pas):
#         valid = True
# print(valid)

# name1= input()
# dob1= input()
# name2= input()
# dob2= input()

# dob1 = dob1.split("-")
# dob2 = dob2.split("-")


# if dob1[2]>dob2[2]:
#     print(name1)
# elif dob1[2]==dob2[2] and dob1[1]>dob2[2]:
#     print(name1)
# elif dob1[2]==dob2[2] and dob1[1]==dob2[2] and dob1[0]>dob2[0]:
#     print(name1)
# elif dob1==dob2:
#     if name1 > name2:
#         print(name2)
#     else:
#         print(name1)
# else:
#     print(name2)

# print("Neha"<"Priya")


# string = input()
# string = string.lower()
# vowels = ['a', 'e', 'i', 'o', 'u']
# res = []
# for char in vowels:
#     if char in string:
#         res.append(char)

# if len(res) > 0:
#     print("".join(res))
# else:
#     print("none")

# id = []
# for i in range(5):
#     id.append(int(input()))
# print(id)
# count = 0
# for i in range(0,len(id)-1):
#     if (id[i]+id[i+1]) %2==0:
#         count +=1
# if count>3:
#     print("Yes")
# else:
#     print("No")


# -------------------------------------------------


# num = input()
# num = num.split(',')
# temp = []
# for i in num:
#     temp.append(int(i))

# # left sum
# left_sum = 0
# for i in range(0, (len(temp)//2)):
#     left_sum += temp[i]

# right_sum = 0
# for i in range((len(temp)//2), len(temp)):
#     right_sum += temp[i]

# if left_sum > right_sum:
#     print("left_heavy")
# else:
#     print("right_heavy")


# def get_column(mat, col):
#     res = []
#     for i in range(len(mat)):
#         if col ==0:
#             res.append(mat[i][0])
#         elif col ==1:
#             res.append(mat[i][1])
#     return res

# # def get_row(mat, row):

# mat= [[1, 2], [3, 4]]
# col = 0
# temp = get_column(mat, col)

# print(temp)


# def insert(L, x):
#     temp = []
#     for i in range(len(L)):
#         if L[i]>x:
#             temp.append(L[i])
#             # L.remove(L[i])

#     for i in range(len(L)-1):
#         if L[i]>x:
#             L.remove(L[i])
#     L.remove(L[-1])
#     L.append(x)
#     L=L+temp
#     return L

# L= [1,2,3,5,6]
# x=4
# print(insert(L,x))


# ----------------------------------------------------------------------------

# def matrix_type(matrix):
#     n = len(matrix)  # get the size of the matrix

#     # check if the matrix is diagonal
#     is_diagonal = True
#     for i in range(n):
#         for j in range(n):
#             if i != j and matrix[i][j] != 0:
#                 is_diagonal = False
#                 break
#         if not is_diagonal:
#             break
#     if is_diagonal:
#         return "diagonal"

#     # check if the matrix is scalar
#     is_scalar = True
#     for i in range(n):
#         for j in range(n):
#             if i == j and matrix[i][j] != matrix[0][0]:
#                 is_scalar = False
#                 break
#             if i != j and matrix[i][j] != 0:
#                 is_scalar = False
#                 break
#         if not is_scalar:
#             break
#     if is_scalar:
#         return "scalar"

#     # check if the matrix is identity
#     is_identity = True
#     for i in range(n):
#         for j in range(n):
#             if i == j and matrix[i][j] != 1:
#                 is_identity = False
#                 break
#             if i != j and matrix[i][j] != 0:
#                 is_identity = False
#                 break
#         if not is_identity:
#             break
#     if is_identity:
#         return "identity"

#     # if none of the above conditions are satisfied, the matrix is non-diagonal
#     return "non-diagonal"


# m = [[1, 2, 3], [4, 1, 6], [7, 8, 1]]
# dig = []
# flag = True
# for i in range(len(m)):
#     for j in range(len(m[0])):
#         if i!=j and m[i][j] != 0:
#            print("it is not a diagonal")
#            flag = False
#            break
#         #    dig.append(m[i][j])
#     if not flag:
#         break
# print(flag)
# # print(dig)

# def matrix_type(M):
#     flag = True
#     scl = True
#     id = True
#     for i in range(len(M)):
#         for j in range(len(M[0])):
#             if i != j and M[i][j] !=0:
#                 flag = False
#                 break
#             elif i ==j and M[i][j] !=M[0][0]:
#                 scl = False
#                 break
#             elif i == j and M[i][j] != 1:
#                 id = False
#                 break
#         if not flag:
#             break

#     if flag and id:
#         return "identity"
#     elif flag and scl:
#         return "scalar"
#     elif flag :
#         return "diagonal"
#     else:
#         return "non-diagonal"

# def matrix_type(M):
#     flag = False
#     temp = []
#     n = len(M)
#     for i range(n):
#         for j in range(n):
#             if i !=j:
#                 if M[i][j] != 0:
#                     flag = True
#                     break
#             elif i==j:
#                 temp.append(M[i][j])
#     if flag:
#         return "non-diagonal"
#     elif all(i ==1 for i in temp:
#         return "identity"
#     elif all(i==temp[0] for i in temp:
#         return "scalar"
#     else:
#         return "diagonal"


# li  = [1,2,3,4,5]
# k=3
# temp = []
# for i in li[k-1::-1]:
#     temp.append(i)
# for i in li[k:len(li)]:
#     temp.append(i)

# print(temp)


# arr = [1, 2, 4, 2, 7, 9, 5, 4, 7,8]
# n = len(arr)
# k = 3
# li = []
# for i in range(k):
#     li.append(arr[i])
# res = []
# res.append(max(li))
# print(li)
# for i in range(k, n):
#     li.remove(li[0])
#     li.append(arr[i])
#     res.append(max(li[0], li[1], li[2]))
# print(res)
# print(li)


# arr = [1001,2002,3003,5005,6006,3121]


# for i in range(len(arr)):
#     dig = []
#     while arr[i]>0:
#         dig.append(arr[i]%10)
#         arr[i]= arr[i]//10
#     temp =-1
#     flag = True
#     for i in range(0,len(dig)//2):
#         if dig[i]==dig[temp]:
#             temp -=1
#         else:
#             flag = False
#             break

# print(flag)
# print(dig)
# print(len(dig)//2)


# def sor(A,B):
#     A.sort()
#     B.sort()
#     print(A)
#     for i in range(len(A)):
#         if A[i] != B[i]:
#             return False
#     else:
#         return True

# A=[1,2,5,4,0]
# B=[2,4,5,0,1]
# print(sor(A,B))


# def merge(D1, D2, p):
#     delete = []
#     for key in D1.keys():
#         if key in D2 and p == "first":
#             delete.append(key)
#         elif key in D2 and p == 'second':
#             delete.append(key)
#     for key in delete:
#         if p == 'first':
#             del D2[key]
#         elif p == 'second':
#             del D1[key]

#     D = {**D1, **D2}
#     print(D)


# def merge(D1, D2, priority):
#     keys_to_delete = []
#     for key in D1.keys():
#         if key in D2:
#             keys_to_delete.append(key)

#     for key in keys_to_delete:
#         if priority == 'first':
#             del D2[key]
#         elif priority == 'second':
#             del D1[key]
#     D = { **D1, **D2 }
#     return D

# D1 = {'a': 1, 'b': 2}
# D2 = {'a': 10, 'c': 3}
# P = 'second'
# print(merge(D1, D2, P))


# def minor_matrix(M, i, j):
#     for x in range(len(M)):
#         row = []
#         if x == i:
#             continue
#         for y in range(len(M[0])):
#             if y !=j:
#                 row.append(M[x][y])
#         print(*row,sep = ',')

# M = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# i = 0
# j = 1

# minor_matrix(M, i, j)


# n = int(input())
# station_dict = {}
# for tr in range(n):
#     name_train = input()
#     m = int(input())
#     compartment_dict = {}
#     for cl in range(m):
#         coach = input().strip().split(',')
#         compartment = coach[0].strip()
#         num_psng = int(coach[1].strip())
#         compartment_dict[compartment]=num_psng
#     station_dict[name_train]=compartment_dict
# print(station_dict)
# print('\n',compartment)
# print('\n',compartment_dict)
# print('\n',num_psng)
# print('\n',coach)
# print('\n',coach)


# names = ["6", "Harsh", "Gaurav", "GauravMiglani", "HarshAgarwal", "GeeksforGeeksGeeks","Programmiz"]
# t, n = 0, 0
# for i in range(len(names)):
#     k = len(names[i])
#     if t < k:
#         t = k
#         n = i
# print(names[n])


# class Solution:
#     def findElements(self,a, n):
#         a.sort()
#         b=a[-1::-1]
#         c=b[2:]
#         return c[-1::-1]

# n=19
# ans = str(n)+str(n*2)+str(n*3)
# temp = []
# for i in ans:
#     temp.append(int(i))
# count =1
# temp.sort()
# for i in temp:
#     if i !=count:
#         print(False)
#     else:
#         count +=1
# else:
#     print(True)


# a = [4, 2, 7]
# b = [5, 6, 3]
# x, y = 0, 0
# for i in range(len(a)):
#     if a[i] > b[i]:
#         x += 1
#     elif a[i] < b[i]:
#         y += 1
# print(x, y)

# def min(li):
#     m = li[0]
#     for i in li:
#         if m > i:
#             m = i
#     return m


# def sort(li):
#     m = min(li)
#     print(m)
#     li.remove(m)
#     return [m] + sort(li)


# li = [5, 4, 3, 8, 9, 2]
# print(sort(li))


# ........................binary search

# def binary_sort(li, key):
#     start = 0
#     end = len(li)-1
#     while start<=end:
#         mid = (start+end)//2
#         if li[mid] == key:
#             return mid
#         elif li[mid] > key:
#             end = mid-1
#         else:
#             start = mid+1
#     return -1 


# li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# n = 9
# print(binary_sort(li, n))



#                  recursive binary search

def rec_binary(l,key,start,end):
    if start>end:
        return -1
    else:
        mid = (start+end)//2
        if l[mid]==key:
            return mid
        elif l[mid]>key:
           return rec_binary(l,key,start,mid-1)
        else:
           return rec_binary(l,key,mid+1,end)

li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 8
print(rec_binary(li, n,0,len(li)-1))





