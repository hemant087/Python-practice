# # r = open('random.txt','r')
# # words = r.read()
# # # print(s)
# # print(words)

# # count =0
# # for i in words:
# #     if i.lower():
# #         count +=1

# # r.close()

# # print(count)


# # file = open('line.txt','r')
# # # l = file.read()
# # line = file.readlines()
# # # print(l)
# # print(line[3-1])

# # file = open('line.txt')
# # word = file.readline()
# # line = word.read()
# # print(len(file))
# # print(len(word))

# # for i in range


# record ={}
# for i in range(4):
#     name = input("Enter your name : ")
#     age = input("Enter your age : ")

#     record[i] = [name,age]


# file = open('record.txt', mode = 'w')
# for i in record:
#     print(f'{i}. my name is {record[i][0]} and my age is {record[i][1]}')
#     file.write(f'{i}. my name is {record[i][0]} and my age is {record[i][1]}\n')


# file.close()


# def spiral_iterative(left, right, n):
#     for i in range(n):
#         center_x = left + (i + 1/2) * (right - left)
#         left = center_x - (right - center_x)
#         right = center_x + (right - center_x)
#     return right

# def spiral_recursive(left, right, n):
#     if n == 0:
#         return left
#     center_x = left + (n - 1/2) * (right - left)
#     return spiral_recursive(center_x - (right - center_x), center_x + (right - center_x), n-1)


# 'file.txt'


# -----------------------------------------------------------------

file = open('file.txt', 'r')
num = file.readlines()
temp = 0
ans = 0
# print(file.read())
for No,line in enumerate(num,1):
    length = len(line.rstrip())
    # print(i)
    # i.strip()
    print(f"{No} :  {length} : {line}")
print(line.strip(),end = ' ')
print(len(int(line.strip())))
if temp < length:
    ans = line
    temp = length

print(ans)
print(ans,temp,"final answer")
print(len(num))


# _____________________________________________________________


# list = [3,1,2,4.5]


# for i in range(len(list)-1):
#     for j in range(len(list)-i-1):
#         if list[j]>list[j+1]:
#             list[j],list[j+1]=list[j+1],list[j]
# print(list)


# Accept input for n
# n = int(input("Enter n: "))

# # Accept input for matrix A
# A = []
# for i in range(n):
#     row = list(map(int, input().split(',')))
#     A.append(row)
# print(A)
# # Accept input for matrix B
# B = []
# for i in range(n):
#     row = list(map(int, input().split(',')))
#     B.append(row)

# print(B)
# # Compute the sum of matrices A and B
# result = []
# for i in range(n):
#     row = []
#     for j in range(n):
#         row.append(A[i][j] + B[i][j])
#     result.append(row)
# print(result)

# # Print the result in the desired format
# for row in result:
#     print(",".join(str(element) for element in row))

# _______________________________________________________________________________________


# n = int(input())
# mat = []
# for i in range(n):
#     temp = list(map(int, input().split(',')))
#     mat.append(temp)
# key = list(map(int, input().split(',')))

# # List to maintain all nearest points
# min_list = []
# min_dist = 1000
# for i in range(n):

#     # Compute the distance
#     dist = (key[0]-mat[i][0])**2 + ((key[1]-mat[i][1])**2)**0.5
#     # Check if it is the minimum distance
#     if (dist < min_dist):
#         min_dist = dist
#         min_list = [mat[i]]
#     elif dist == min_dist:
#         min_list.append(mat[i])
# for point in min_list:
#     print(point)


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



# _______________________________________________________________________


record = open('subRecord.txt','a')
data = input()
record.write(data)
