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

# def rec_binary(l,key,start,end):
#     if start>end:
#         return -1
#     else:
#         mid = (start+end)//2
#         if l[mid]==key:
#             return mid
#         elif l[mid]>key:
#            return rec_binary(l,key,start,mid-1)
#         else:
#            return rec_binary(l,key,mid+1,end)


# def member(L, x):
#     if len(L) == 0:
#         return False
#     if len(L) == 1:
#         return L[0] == x
#     return member(L[: -1], x)


# L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(member(L, 8))
# n = 8
# print(rec_binary(li, n,0,len(li)-1))

# def sum(n):
#     if n ==0:
#         return
#     else:
#         print(n,end=",")
#         sum(n-1)
#         print(n)
#         return
# sum(5)

# l = [1, 2, 3, 4, 5]

# def sort(l,key):
#     if key == l[len(l)]:
#         return 1
#     else:


#                        tower of hanoi


# def towerOfHanoi(n,s,h,d):
#     if n==1:
#         print("\n1st disc is moved from ",s," to ",d)
#         return
#     towerOfHanoi(n-1,s,d,h)
#     print("\n",f"{n}th term is move from", s,"to",d)
#     towerOfHanoi(n-1,h,s,d)


# towerOfHanoi(4,'source','helper','destination')


# .........................................replace string by using recursion


# def replace(l,a,g):
#     if len(l)==0:
#         return l
#     smallest = replace(l[1:],a,g)
#     if l[0]==a:
#         return g+smallest
#     else:
#         return l[0]+smallest

# print(replace('haa haa haa ! ','a','g'))


# str = "[({()})]"
# stack = []

# for i in str:
#     if i =="("or i=="{"or i=='[':
#         stack.append(i)
#     else:
#         if len(stack)==0:
#             return False
#         top = stack[len(stack)]


# def gfSeries(N):

#     if N == 1:
#         return [0]
#     elif N == 2:
#         return [0,1]
#     else:
#         prTerm = gfSeries(N-1)
#         cuTerm = (prTerm[-2]**2-prTerm[-1])
#         prTerm.append(cuTerm)
#         return prTerm


# print(gfSeries(6))

# arr= [2,4,6,6,6,6,6,6,6,7,9,0,3]
# x=6
# ans = []
# ans.extend([i for i in range(len(arr)) if arr[i]==x])
# print(ans)


# def minDist(self, arr, n, x, y):
#         first = 0
#         second =0
#         for i in range(len(arr)):
#             if x == arr[i]:
#                 first = i
#             elif y == arr[i]:
#                 second = arr[i]
#         return min(abs(first-second),abs((len(arr)-second)+first))


# arr = [1,2,3,4,5,6,7,8,5,4,3,5,6,7,88,5,5,]


# arr.insert(0,arr[-1])
# arr.pop(arr[-1])
# print(arr)


# arr = [1, 97, 14, 4, 6, 66, 94, 40, 49, 68, 16, 36, 20, 38, 25, 31, 12,
#        42, 52, 28, 67, 87, 16, 87, 27, 67, 34, 4, 76, 45, 38, 76, 41, 51, 31]
# a, b = 97, 67

# if a and b not in arr:
#             print(-1)
# f = arr.index(a)
# s = arr.index(b)
# x=abs(f-s)
# y=abs((len(arr)-arr.index(b))+arr.index(a))
# print([x,y], "<---- here")
# print(min(x,y))

# if a not in arr or b not in arr:
#     print(-1)

# flag = None
# for i in range(len(arr)):
#     if arr[i] == a or arr[i] == b:
#         if flag is not None and arr[i] != flag:
#             print(i - flag)
#             break
#         flag = i
# else:
#     print(-1)


# def Maximize(self, a, n):
#     # Complete the function
#     sum1 = 0
#     for i in range(len(a)):
#         sum1 += a[i]*i
#     a = a[len(a):0:-1]
#     sum = 0
#     for i in range(len(a)):
#         sum += a[i]*i
#     return max(sum, sum1)

# sum1 = 0
# for i in range(len(a)):
#     sum1 += a[i]*i
# # a = a[len(a):0:-1]
# a.sort()
# sum = 0
# for i in range(len(a)):
#     sum += a[i]*i
# print(max(sum, sum1))
# print(sum,sum1)

# print(Maximize(a,len(a)))


# ----------------------------------------------------------------------------

# arr = [1, 2, 3, 4, 5, 6, 7]
# d = 2
# n = len(arr)
# for i in range(d // 2):
#        arr[i], arr[d-i-1] = arr[d-i-1], arr[i]

# # Reverse the remaining n-d elements
# for i in range(d, (n+d)//2):
#        arr[i], arr[n+d-i-1] = arr[n+d-i-1], arr[i]

# # # Reverse the entire array
# for i in range(n // 2):
#        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]

# for i in range(d):
#     temp = arr[0]
#     arr.remove(arr[0])
#     arr.insert(n+1,temp)

# Output: 3 4 5 6 7 1 2
# print(arr)

# n=5
# a=0
# b=1
# for i in range(n):
#     print(a)
#     temp = a
#     a = b
#     b = temp+b


# ----------------------------------------------------------------------------------


# s = 'Geeks'
# ans=s[::-1]
# print(ans)


# ----------------------------------------------------------------------


# n = '1005'
# for i in n:
#     if i == '0':
#         i,i = '5','0'
# print(n)


# list = ['1','2','3','4','5','6','7','8','9']
# y = enumerate(list)
# print(y)

# ----------------------------------------------------------------

# record = {'hemant': 10, 'rahul': 20, 'rajeev': 30, 'vishal': 40}
# num = int(input("enter the number of student: "))
# i = 1
# while num>=i:
#        name = input("Enter student name: ")
#        marks = int(input("Enter the marks: "))
#        record[name] = marks

#        i +=1
# print("here is your record :")
# for i in record:
#        print(i ,"\t", record[i])

# print('\n',record)

# key = input('Enter the name: ')
# print(record.get(key,"dont know!!!!!"))
# print(record.popitem())
# record.popitem()
# print(record)
# print(record.keys())
# print(record.values())

# cop = record.copy()
# cop.setdefault('sunny',50)
# print(cop)


# def fun(n):
#     if n==0:
#         return 0
#     else:
#         return n-1 + fun(n-1)
# print(fun(5))

# word = 'abctcba'
# print(word[1],word[-1])
# for i in range((len(word)//2)+1):
#     if word[i-1]!= word[-i]:
#         print('not palindrome')
#         break
# else:
#     print('palindrome')

# def fun(word):
#     if len(word) <= 2:
#         return True
#     elif word[0] !=word[-1]:
#         return False
#     else:
#         return fun(word[1:-1])

# word = 'abcsdcba'

# print(fun(word))


# def spiral_iterative(left, right, n):
#     point = left
#     dist = right - left
#     for i in range(n):
#         dist /= 2
#         if i % 2 == 0:
#             point += dist * 2
#         else:
#             point -= dist * 2
#         print(point)
#     return float(point)


# def spiral_recursive(left, right, n):
#     mid = (left + right) / 2
#     if n == 0:
#         return left
#     elif n % 2 == 0:
#         return spiral_recursive(mid, right, n - 1)
#     else:
#         return spiral_recursive(left, mid, n - 1)


# print(spiral_iterative(0,1,4))
# print(spiral_recursive(0, 1, 4))


# def fun(left, right,n):
#     for i in range(n-1):
#         mid = (left+right)/2
#         if i%2==0:
#             left = mid
#         else:
#             right = mid
#     print(left)

# def fun(left, right, n):
#     mid = (left+right)/2
#     if n == 0:
#         return left
#     elif n % 2 == 0:
#         return fun(mid, right, n-1)
#     else:
#         return fun(left, mid, n-1)
#     # print(left)


# print(fun(0, 1, 4))


# def count(L, word):
#     if len(L)==0:
#         return
#     elif L[0]==word:
#         cou +=1
#     count =0
#     for i in L:
#         if i ==word:
#             count +=1
#     return count

# print(count(['good', 'string', 'good', 'again', 'good'],'good'))


# def non_decreasing(L):
#     if len(L)==1:
#         return True
#     temp = L[1]
#     if temp < L[0]:
#         print(temp,L[0])
#         return False
#     else:
#         return non_decreasing(L[1:])

# L= [1, 1, 2, 3, 3, 5]

# print( "This is your answer", non_decreasing(L))


# -----------------------------------------------------------------

# num = '5440'
# dig = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',0:'zero'}
# for i in range(len(num)):
#     print(num[i])
#     print(dig[int(num[i])])
# print(dig.get('one'))

# value = 'four'
# dic = []
# for key, val in dig.items():
#     if value == val:
#         print(key)
#         dic.append(key)

# print(dic)
# print(list[4])

# --------------------------------------------------------------------------------------


# words = "apple,and,oranges,are,only,fruits"
# words = words.split(',')
# print(words)
# dic = {}
# # print(words[0][0])
# for word in words:
#     if word[0] in dic:
#         dic[word[0]].append(word)
#     else:
#         dic[word[0]] = [word]
# print(dic)

# words = "apple,and,oranges,are,only,fruits"
# words = words.split(',')
# print(words)
# dic = {}
# for word in words:
#     if word[0] in dic:
#         dic[word[0]].append(word)
#     else:
#         dic[word[0]] = [word]
# print(dic)

# li = [10, 20, 30, 40, 20, 50]


# def reverse(li):
# #     print(li)
#     if len(li)==0:
#         return []
#     else:
#         print(li)
#         return [li[-1]] + reverse(li[:-1])

# print(reverse(li))

# _____________________________________________________________________________________


# n = int(input( 'enter : '))
# L=[]
# ans = []
# temp =[]
# for i in range(n*n):
#         L.append(input().split(','))

# for i in range(n):
#         for j in range(n):
#                 ans.append(int(L[i][j])+int(L[i+n][j]))
#         temp.append(ans)
# print(L)
# print(ans)
# print(temp)

# n = int(input("Enter n: ")) # Input n

# L = []
# ans = []
# temp = []

# # Input matrix A and B
# for i in range(n * n):
#     L.append(input().split(','))

# # Calculate the sum of matrices A and B
# for i in range(n):
#     for j in range(n):
#         ans.append(int(L[i][j]) + int(L[i + n][j]))
#     temp.append(ans)
#     ans = []

# # Print the result in the desired format
# print(temp)
# for i in temp:
#     print(",".join(str(j) for j in i))


# for row in temp:
#     print(",".join(str(element) for element in row))


# n = int(input("Enter n :"))

# A = []
# for i in range(n):
#     temp = list(map(int, input().split(',')))
#     A.append(temp)
# print(A)
# B = []

# for i in range(n):
#     temp = list(map(int, input().split(',')))
#     B.append(temp)

# print(B)

# ans = []
# for i in range(n):
#     k = []
#     for j in range(n):
#         k.append(A[i][j]+B[i][j])
#     ans.append(k)

# print(ans)
# for row in ans:
#     print(",".join(str(element) for element in row))


# n = int(input('enter n :'))

# ans = []
# for i in range(n):
#     k =[]
#     for j in range(n):
#         if i ==j:
#             k.append(1)
#         else:
#             k.append(0)
#     ans.append(k)
# print(ans)


# _____________________________________________________________________________

# n = int(input('enter : '))

# mat = []
# for i in range(n):
#     temp = list(map(int, input().split(',')))
#     mat.append(temp)
# key = list(map(int, input().split(',')))

# all_dis = []
# ans = []
# min_dis = 1000
# for i in range(n):
#     dis = ((key[0]-mat[i][0])**2 + ((key[1]-mat[i][1])**2))**0.5

#     all_dis.append(dis)

#     if dis < min_dis:
#         min_dis = dis
#         ans = [mat[i]]
#     elif dis == min_dis:
#         ans.append(mat[i])

# print(ans)
# # print(key)
# # print(mat)
# print(all_dis)

# ______________________________________________________________________________________

# name = list(map(str, input().split(',')))
# marks = list(map(int, input().split(',')))
# ans = []
# for i in range(len(marks)):
#     for j in range(i, len(marks)):
#         if marks[i] == marks[j] and name[i] != name[j]:
#             temp = [name[i], name[j]]
#             ans.append(temp)

# print(ans)


# ____________________________________________________________________


# n  = int(input('enter : '))

# a = []
# for i in range(n):
#     temp = list(map(int, input().split(',')))
#     a.append(temp)

# b = []
# for i in range(n):
#     temp = list(map(int, input().split(',')))
#     b.append(temp)

# ans = []
# for i in range(n):
#     l = []
#     for j in range(n):
#         temp = 0
#         for k in range(n):
#             temp += a[i][k]*b[k][j]
#         l.append(temp)
#     ans.append(l)

# print(ans)


# ____________________________________________________________________________________


# num = list(map(int,input().split(',')))
# num = sorted(num)
# n = len(num)//2
# print(num)
# if len(num)%2!=0:
#     print(num[n])
# else:
#     print((num[n-1]+num[n])//2)


# _____________________________________________________________________________________


# list = [1,2,3,4,6,7,8]
# key = 5
# list.append(key)

# for i in range(len(list)):
#     for j in range(len(list)):
#         if list[i]<list[j]:
#             list[i],list[j]=list[j],list[i]

# print(list)

# ___________________________________________________________________________________
# def isint(num):
#     if int(num) is int:
#         return True
#     else:
#         return False
# temp = '987o35l7o4'
# temp= input()
# temp[0]
# for i in temp:
#     if isint(i):


# _______________________________________________________________________________________

# L = [1, 3, 11, 18, 17, 23, 6, 8, 10]

# def isPrime(n):
#     if n == 0 or n == 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     else:
#         return True


# def primes_galore(L):
#     count = 0
#     for i in range(len(L)):
#         print(isPrime(i), i)
#         if isPrime(i):
#             print(isPrime(L[i]), L[i])
#             if isPrime(L[i]):
#                 count += 1
#     return count


# def std_dev(X):

#     xi = []
#     s = 0
#     for i in X:
#         s += i
#     mean = s/len(X)
#     print(mean,s)
#     for i in X:
#         xi.append((i-mean)**2)
#     sum1 = 0
#     print(xi)
#     for i in xi:
#         sum1 += i
#     print(sum1)
#     return sum1/len(xi)-1


# X = [1,2,3,4,5,6,7,8,9]
# sigma = std_dev(X)
# print(f'{sigma:.2f}')


# _________________________________________________________________
# list = ["{", "}", "[", "]", "(", ")"]

# def balanced(word):
#     stack = []
#     open = ['(', '{', '[']
#     close = [')', '}', ']']

#     for ch in word:
#         if ch in open:
#             stack.append(ch)
#         elif ch in close:
#             if len(stack) == 0:
#                 return False
#             last = stack.pop()
#             if open.index(last) != close.index(ch):
#                 return False

#     if len(stack) == 0:
#         return True
#     else:
#         return False

# print(balanced([]))


# lat = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
# cod = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n']

# str = 'apply'
# temp =''

# for i in str:
#     if i in lat:
#         temp += cod[lat.index(i)]
#         print(i)
#     else:
#         temp += lat[cod.index(i)]
#         print(i)

# print(str)
# print(temp)


# _____________________________________________________________________


# list = [1,2,3,4,5,6,7,8,9]

# def swift(list,term):
#     for i in range(term):
#         num = list.pop()
#         list.insert(0,num)

#     return list

# print(swift(list,4))


# _______________________________________________________________________


# A=[[1,2,3],[4,5,6],[7,8,9]]
# B=[[9,8,7],[6,5,4],[3,2,1]]
# C=[[1,0,1],[1,0,1],[1,0,1]]
# D=[[10,0,10],[10,0,10],[10,0,10]]


# def product(a,b):
#     result = []
#     for i in range(len(a)):
#         ans = []
#         for j in range(len(a[0])):
#             temp =0
#             for k in range(len(a)):
#                 temp += a[i][k]*b[k][j]
#             ans.append(temp)
#         result.append(ans)
#     return result


# temp = product(A,B)
# temp2 = product(temp,C)
# temp3 = product(temp2,D)
# print(temp3)


# ________________________________________________________________________________________

# import string

# # l = string.ascii_lowercase
# l = list(string.ascii_lowercase)
# p = list(string.ascii_uppercase)
# # print(l)
# # print(p)

# for No,i in enumerate(l,1):
#     l[i]  =
#     print(f'{No} : {i}')

# _________________________________________________________________________________________________


# def fun(limit):
#     for i in range(limit):
#         yield i


# print(next(fun(4)))
# print(next(fun(4)))
# print(next(fun(4)))
# print(next(fun(4)))


# def fen(n):
#     for i in range(n):
#         yield i*i
# h = fen(4)
# for i in range(4):
#     print(next(h))


# ________________________________________________________________________________


# for i in range(2, 7):
#     for j in range(1, i+1):
#         print(j, end=' ')
#     for j in range(i-1, 0, -1):
#         print(j, end=' ')
#     print()


# coin = int(input())
# a = int(input())
# b = int(input())
# c = int(input())

# if a!=b and b!=c and c!=a and a+b+c == coin and a!=0 and b!=0 and c!=0:
#     print('FAIR')
# else:
#     print('UNFAIR')
# x = '1.5'
# print(int(x[0]))


# -------------------------------------------------------------------------------------



# x = " hii i ma hemant raj let check "
# ans = []
# for i in x:
#     if i in ['a','e','i','o','u']:
#         continue
#     else:
#         ans.append(i)

# ' '.join(ans)
# print(ans)



# =====



# for char in 'a1b2c3d4e5':    
#     if char in 'abcde':
#         print('|', end = '') # there is no space between the quotes
#         continue    
#     print(char, end = '')  # there is no space between the quotes
# print('|')

# ==============================================


# x= int(input())
# y =0
# while x > 1:
#     x = x//2
#     y +=1
# print(y) 



# ==================================================



# string = 'no sentence can begin with because because because is a conjunction'

# key = 'because'
# # str = list(map(int, string.split(' ')))
# string = string.split(' ')
# a = 0
# flag = False
# for i in string:
#     if key ==i:
#         a +=1
#         flag = True

# if flag:
#     print('YES')
#     print(a)
# else:
#     print('NO')

# ===========================================================

# marks = [60,10,30,40,20,50]

# for i in range(len(marks)):
#     for j in range(i+1 , len(marks)):
#         if marks[i]> marks[j]:
#             marks[i],marks[j] = marks[j],marks[i]
# n = len(marks)
# if n % 2==1:
#     print((marks[n//2]+ marks[(n//2)+1])//2)
# else:
#     print(marks[n//2])



# ===========================================================



n = int(input())
mat =[]
for j in range(n):
    temp =[]
    for a in range(n):
        temp.append(list(map(int,input().split(','))))
    mat.append(temp)


print(mat)

# multiplication
mat1 =[[0,0],[0,0]]
for i in range(n):
    for j in range(n):
        for k in range(n):
           mat1[i][j] += mat[0][j][k]*mat[1][k][j]

print(mat1)