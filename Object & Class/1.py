# # class Bank:
# #     def __init__(self,a,b):
# #         self.accNo=a
# #         self.balance = b

# # ac1= Bank(100,30000)

# # print(ac1.__dict__)


# # class Students:
# #     def __init__(self,name,age):
# #         self.name=name
# #         self.age=age
# #         print("My name is {}".format(self.name))
# #         print("and i'm {} years old".format(age))
# #         # print("This is Address of self ", id(self))

# # s1= Students("Hemant Raj", 19)

# # print(id(Students))
# # print(id(s1))
# # print()


# # /------------------------------------------

# # Inheritance
# # Inheritance is the capability of one class to derive or inherit the properties from another class. The class that derives properties is called the derived class or child class and the class from which the properties are being derived is called the base class or parent class. The benefits of inheritance are:

# # It represents real-world relationships well.
# # It provides the reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
# # It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.
# # Types of Inheritance –
# # Single Inheritance:
# # Single-level inheritance enables a derived class to inherit characteristics from a single-parent class.

# # Multilevel Inheritance:
# # Multi-level inheritance enables a derived class to inherit properties from an immediate parent class which in turn inherits properties from his parent class.

# # Hierarchical Inheritance:
# # Hierarchical level inheritance enables more than one derived class to inherit properties from a parent class.

# # Multiple Inheritance:
# # Multiple level inheritance enables one derived class to inherit properties from more than one base class.


# # class Person:
# #     def __init__(self, name, id):
# #         self.name = name
# #         self.id = id

# #     def temp(self):
# #         print(self.name)
# #         print(self.name)

# # # childe class


# # class employ(Person):
# #     def __init__(self, name, id, location, work):
# #         self.location = location
# #         self.work = work
# #         # inheriting the property
# #         Person.__init__(self, name, id)

# #     def display(self):
# #         print(self.location)
# #         print(self.work)


# # # p1 = Person()
# # e1 = employ("hemant", 587, 'maranga', 'sd1')

# # # e1.temp()
# # # e1.display()

# # print(e1.__dict__)
# # # print(p1.__dict__)


# class Student:
#     def __init__(self,name,id):
#         self.name= name
#         self.id=id
#     def show(self):
#         print("My name is {} and".format(self.name))
#         print("My id is {} and".format(self.id))

#         # Student.__init__(self,name,id)

# # class Staff(Student):
# #     def __init__(self, name, id,position,sealery):
# #         self.position=position
# #         self.sealery=sealery
# #         # self.name=name
# #         # self.id= id
# #         Student.__init__(self,name,id)

# #     def display(self):
# #         print(self.name)
# #         print(self.id)
# #         print(self.position)
# #         print(self.sealery)


# # s1=Staff('hemant',587,'student',2000)
# # s1.display()
# # s1.show()
# # Staff.__dict__()


# # ...........................Calculator........................................


# class calculator():
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
# class addition(calculator):
#     def add(self,num1,num2):
#         print("{} + {} = {}".format(num1,num2,num1+num2))
#         calculator.__init__(self,num1,num2)
# class subtractions(calculator):
#     def sub(self,num1,num2):
#         print("{} - {} = {}".format(num1,num2,num1-num2))
#         calculator.__init__(self,num1,num2)
# class multiplication(calculator):
#     def multi(self,num1,num2):
#         print("{} x {} = {}".format(num1,num2,num1*num2))
#         calculator.__init__(self,num1,num2)


# num1=int(input())
# num2=int(input())

# cl=addition(num1,num2)
# cl.add()


# =================================================================


# n = int(input())
# L = []
# # Append all points in the sequence to the list L
# for i in range(n):
#     L.append(input())
# # Point P
# point = input().split(',')
# x = int(point[0])
# y = int(point[1])
# # List to maintain all nearest points
# min_list = []
# min_dist = 1000
# for i in range(n):
#     # One of the points in the sequence
#     temp = L[i].split(',')
#     # Extract the x and y coordinates of this point
#     temp_x = int(temp[0])
#     temp_y = int(temp[1])
#     # Compute the distance
#     dist = ((x - temp_x) ** 2 + (y - temp_y) ** 2) ** 0.5
#     # Check if it is the minimum distance
#     if (dist < min_dist):
#         min_dist = dist
#         min_list = [L[i]]
#     elif dist == min_dist:
#         min_list.append(L[i])
# for point in min_list:
#     print(point)


# ====================================================================


# l= [1,2,3,6,4,6,5]
# new = []
# for i in range(3):
#     new.append(max(l))
#     l.remove(max(l))
# print(new)
# print(l)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++


# n =10
# priv = 0
# curr = 1
# for i in range(n):
#     if n<2:
#         print(1)
#     else:
#         next = priv + curr
#         priv = curr
#         curr = next
#         print(curr)


# ======================================================================


# L= [1,2,3,5,6,7]
# x=4
# L.append(x)
# for i in range(len(L)):
#     for j in range(i+1,len(L)):
#         if L[i]>L[j]:
#             L[i],L[j]=L[j],L[i]
# print(L)


# ====================================================================

# word_2 = 'Dog'
# word_1= 'cat'
# word_1 = word_1.lower()
# word_2 = word_2.lower()
# sum = 0
# for i in range(len(word_1)):
#     sum = sum + abs(ord(word_1[i])-ord(word_2[i]))
# print(sum)


# ======================================================================
# mat = [[4,9, 2],[3, 5, 7],[8, 1, 6]]
# mat = [[1,2],[2,1]]


# row = []
# for i in range(len(mat)):
#     sum = 0
#     for j in range(len(mat[0])):
#         sum = sum + mat[i][j]
#     row.append(sum)

# col = []
# for i in range(len(mat)):
#     sum = 0
#     for j in range(len(mat[0])):
#         sum = sum + mat[j][i]
#     col.append(sum)

# dig = 0
# for i in range(len(mat)):
#     for j in range(len(mat[0])):
#         if i == j:
#             dig = dig + mat[i][j]

# print(row,col,dig)

# if col == row and col[0]==dig:
#     print('Yes')
# else:
#     print('No')


# ===========================================================

# mat = [[4,9, 2],[3, 5, 7]]

# tran = []
# for i in range(len(mat[0])):
#     temp = []
#     for j in range(len(mat)):
#         temp.append(mat[j][i])
#     tran.append(temp)

# print(tran)

# =========================================================

# num = input()
# num = '987o35i7o4'
# num = num.split('o')
# print(num)
# temp = []
# for i in range(len(num)):
#     temp.append(num[i])
#     temp.append('0')

# del temp[-1]

# num = "".join(temp)

# num = num.split('i')
# temp = []
# for i in range(len(num)):
#     temp.append(num[i])
#     temp.append('1')

# del temp[-1]

# num = "".join(temp)
# print(num)

# ============================================================


# num = ['1,2,3,4,5,6']
# num = ['1,1,1,1']
# new_num = list(int(i) for i in num[0].split(','))
# print(new_num)

# num = [int(i) for i in num[0].split(',')]
# print(num)
# first = sum(num[0:len(num)//2])
# second = sum(num[len(num)//2:])
# print(first,second)


# ===============================================================

# m = [
#     [5, 0, 0],
#     [0, 5, 0],
#     [0, 0, 5]
# ]
# m = [[2, 0, 0, 0],
#      [0, 2, 0, 0],
#      [0, 0, 3, 0],
#      [0, 0, 0, 2]]

# def matrix_type(m):
#     if len(m) != len(m[0]):
#         return 'non-diagonal'
#     for i in range(len(m)):
#         for j in range(len(m[0])):
#             if i != j and m[i][j] != 0:
#                 return 'non-diagonal'
#         if m[i][i] == 1:
#             return 'identity'
#         if m[i][i] != 1 and m[i][i] != 0 and m[i][i] == m[0][0]:
#             return 'scaler'
#     else:
#         return 'diagonal'
# print(matrix_type(m))


# def matrix_type(M):
#     rows = len(M)
#     cols = len(M[0])

#     # Check if the matrix is square (rows == cols)
#     if rows != cols:
#         return 'non-diagonal'

#     # Check if the matrix is diagonal
#     is_diagonal = all(M[i][j] == 0 for i in range(rows) for j in range(cols) if i != j)
#     if is_diagonal:
#         # Check if it is a scalar matrix
#         diagonal_element = M[0][0]
#         is_scalar = all(M[i][i] == diagonal_element for i in range(rows))
#         if is_scalar:
#             # Check if it is an identity matrix
#             if diagonal_element == 1:
#                 return 'identity'
#             else:
#                 return 'scalar'
#         else:
#             return 'diagonal'
#     else:
#         return 'non-diagonal'

#     for i in


# ========================================================================

# para  = "good word many good works good real choice"
# n = 3

# def exact_count(para, n):
#     temp = []
#     para = para.split(' ')
#     for i in range(len(para)):
#         count = para.count(para[i])
#         temp.append(count)

#     if n in set(temp):
#         return 'True'
#     else:
#         return 'False'


# print(exact_count(para, n))


# =====================================================================

# num = '12345'
# temp = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
# for i in range(len(num)):
#     print(temp[int(num[i])])

# =================================================================

# D = {1: 10, 2: 100, 3: 1000, 4: 10}
# value = 10


# def value_to_keys(D, value):
#     temp = []
#     for i in D:
#         if value == D[i]:
#             temp.append(i)
#     print(temp)


# print(value_to_keys(D, value))

# =================================================================

# D = {5: 10, 2: 100, 3: 1000, 4: 10}
# def dict_to_list(D):
#     count = len(D)
#     temp = []
#     for i in D.keys():
#         temp.append((i,D[i]))
#     return temp

# print(dict_to_list(D))

# L = [(5, 10), (2, 100), (3, 1000), (4, 10)]

# def list_to_dict(L):
#     dic = {}
#     for i in range(len(L)):
#         dic[L[i][0]]= L[i][1]
#     return dic
# print(list_to_dict(L))

# ===============================================================================

# dataset = [{'SeqNo': 1, 'Name': 'Devika', 'Gender': 'F', 'City': 'Bengaluru', 'Mathematics': 85, 'Physics': 100, 'Chemistry': 79, 'Biology': 75, 'Computer Science': 88, 'History': 60, 'Civics': 88, 'Philosophy': 95}, {'SeqNo': 18, 'Name': 'Hemant', 'Gender': 'F', 'City': 'Purnea', 'Mathematics': 85, 'Physics': 100,
#     'Chemistry': 79, 'Biology': 75, 'Computer Science': 88, 'History': 55, 'Civics': 88, 'Philosophy': 95}, {'SeqNo': 13, 'Name': 'Rahul', 'Gender': 'F', 'City': 'Bengaluru', 'Mathematics': 85, 'Physics': 100, 'Chemistry': 79, 'Biology': 75, 'Computer Science': 88, 'History':57, 'Civics': 88, 'Philosophy': 95}]


# def crowded_group(scores_dataset, subject, mark_limit):
#     count = 0
#     for i in range(len(scores_dataset)):
#         for j in range(i+1,len(scores_dataset)):
#             if abs(scores_dataset[i][subject] - scores_dataset[j][subject]) <= mark_limit:
#                 count +=1

#     return count

# print(crowded_group(dataset,'History',2))

# =====================================================================================


# def group_by_city(scores_dataset):
#     dic = {}
#     for i in scores_dataset:
#         if i['City'] in dic:
#             dic[i['City']].append(i['Name'])
#         else:
#             dic[i['City']] = [i['Name']]
#     return dic


# def busy_cities(scores_dataset):
#     dict = group_by_city(scores_dataset)


#     # max_value_length = max(len(value) for value in dict.values())
#     maximum = []
#     for value in dict.values():
#         maximum.append(len(value))


#     # keys_with_max_length = [key for key, value in dict.items() if len(value) == max_value_length]
#     max_len_key = []
#     for key, value in dict.items():
#         if len(value)  == max(maximum):
#             max_len_key.append(key)


#     # return ("Keys with the maximum value length:", keys_with_max_length)
#     return max_len_key

# dic = {}
# for i in dict:
#     dic[i] = len(dict[i])
# print(dic)
# temp = []
# for i in dic:
#     if max(len(dic[i])) == len(dic[i]):
#         temp.append(i)
# print(temp)

# =========================================================================
# str = ['apple', 'and', 'oranges', 'are', 'only', 'fruits']
# real_dict = {}
# for i in str:
#     if i[0] in real_dict:
#         real_dict[i[0]].append(i)
#     else:
#         real_dict[i[0]] = [i]
# print(real_dict)


# =================================================================
# def marks(scores_dataset, subject, gender):
#     temp = {}
#     for data in scores_dataset:
#         if data['Gender'] == gender:
#             temp[data['Name']] = data[subject]
#     return temp


# def get_toppers(scores_dataset, subject, gender):
#     marks_dataset =  marks(scores_dataset, subject, gender)
#     max_marks = max(marks_dataset.values())

#     ans = []
#     for name , mark in marks_dataset.items():
#         if mark == max_marks:
#             ans.append(name)
#     return ans

# ======================================================================


# dataset = [{
#     'TID': 'Gurunath_8528',
#     'Items': [
#         {'Name': 'Notebook', 'Price': 50, 'Qty': 4},
#         {'Name': 'Pencil', 'Price': 10, 'Qty': 1},
#         {'Name': 'Eraser', 'Price': 15, 'Qty': 1},
#         {'Name': 'File', 'Price': 80, 'Qty': 1}
#     ]
# },{
#     'TID': 'Hemant',
#     'Items': [
#         {'Name': 'Notebook', 'Price': 50, 'Qty': 4},
#         {'Name': 'Pencil', 'Price': 12, 'Qty': 1},
#         {'Name': 'Eraser', 'Price': 105, 'Qty': 1},
#         {'Name': 'File', 'Price': 80, 'Qty': 1}
#     ]
# }]


# def total_price(Items):
#     sum = 0
#     for th in Items:
#        sum +=  th['Price']*th['Qty']
#     return sum


# ans = {}
# for item in dataset:
#     ans[item['TID']] = total_price(item['Items'])
# print(ans)


# ===============================================================================

# words = ['a', 'random', 'collection', 'a', 'another', 'a', 'random']
# def freq_to_words(words):
#     dict = {}
#     for w in words:
#         dict[w] = words.count(w)
#     print(dict)
#     new_dict = {}
#     for chr ,frq in dict.items():
#         if frq in new_dict:
#             new_dict[frq].append(chr)
#         else:
#             new_dict[frq] = [chr]
#     return new_dict


# print(freq_to_words(words))


# =============================================================================


# m = [[1, 2, 3], [4, 5, 6]]   # need to do transpose
# ans = []
# for i in range(len(m[0])):
#     temp = []
#     for j in range(len(m)):
#         temp.append(m[j][i])
#     ans.append(temp)

# mat = []
# for row in ans:
#     mat.append(row[::-1])
# print(mat)

# ==========================================================================

# dataset = [('Harish', 80), ('Aparna', 90), ('Harshita', 80)]

# new_dataset = []

# while dataset !=[]:
#     min_data = dataset[0]
#     for i in range(len(dataset)):
#         if dataset[i][1] < min_data[1]:
#             min_data = dataset[i]
#         elif dataset[i][1] == min_data[1] and dataset[i][0]<min_data[0]:
#             min_data = dataset[i]
#     new_dataset.append(min_data)
#     dataset.remove(min_data)
# print(new_dataset)


# def two_level_sort(scores):
#     sorted_scores = []
#     while scores:
#         min_entry = scores[0]  # Initialize min_entry with the first tuple in the scores list
#         for entry in scores:
#             if entry[1] < min_entry[1]:  # Compare the score of each tuple with the score of min_entry
#                 min_entry = entry  # If the score is lower, update min_entry to the current entry
#             elif entry[1] == min_entry[1] and entry[0] < min_entry[0]:  # Compare names if scores are equal
#                 min_entry = entry  # If the name is lexicographically smaller, update min_entry
#         sorted_scores.append(min_entry)  # Append the minimum tuple to sorted_scores
#         scores.remove(min_entry)  # Remove the minimum tuple from scores to find the next minimum
#     return sorted_scores

# print(two_level_sort(dataset))

# =====================================================================================================


# def is_reachable(grid):
#     ib = 0
#     ig = 0
#     jb = 0
#     jg = 0

#     step = 0
#     for i in range(len(grid)):
#         for j in range(len(grid)):
#             if grid[i][j] == 'B':
#                 ib = i
#                 jb = j
#             if grid[i][j] == 'G':
#                 jg = j
#                 ig = i
#     if ib>=ig and jb<=jg:
#         step = (ib-ig)+(jg-jb)
#         return (True,step)
#     else:
#         return (False,None)


# ======================================================================================================

# num = input()
# temp = []
# for i in num:
#     temp.append(int(i))
# print(temp)
# ans = []
# for i in range(len(temp)//2):
#     ans.append(temp[i]+temp[i+(len(temp)//2)])

# print(max(ans))

# ======================================================================================
# players = { 'Hemant':{'a':True,'b':True,'c':False},'Rahul':{'a':True,'b':False,'c':False},'Hemant1':{'a':True,'b':True,'c':False},'Rahul1':{'a':True,'b':False,'c':False},'Hemant2':{'a':True,'b':True,'c':False},'Rahul2':{'a':True,'b':True,'c':False},}

# def exactly_two(players):
#     for name,data in players.items():
#         if (data['a'] == True and data['b'] ==True and data['c'] == False)
#         elif (data['b'] == True and data['c'] == True)
#         elif(data['a']== True and data['c'])


# exactly_two(players)


# ======================================================================================

# def mentors(scores_dataset,subject):
# need_data = []
# for data in scores_dataset:
#     need_data.append(([data['SeqNo']] , data[subject]))

# ans = {}
# for i in range(len(need_data)):
#     ans[need_data[i][0]] = []
#     for j in range(len(need_data)):
#         if 10 <= (need_data[i][1] - need_data[j][1]) <= 20 and i !=j:
#             ans[need_data[i][0]].append(need_data[j][0])
# return ans
# D = dict()
# for a in scores_dataset:
#     D[a['SeqNo']] = []
#     for b in scores_dataset:
#         if 10 <= a[subject]-b[subject] <= 20:
#             print(b['SeqNo'])
#             D[a['SeqNo']].append(b['SeqNo'])
# return D


# results = []
# for i in range(8):
#     L = input().split(',')
#     winner = L[0]  # the first team is the winner
#     losers = L[1:]  # all these teams have lost to the winner
#     # we only need the number of wins and the winning team
#     results.append((winner, len(losers)))
# table = []
# # two-level-sort
# # refer GrPA-4 of week-6
# # we first sort by points, then by name
# while results != []:
#     maxteam = results[0]
#     for i in range(len(results)):
#         team = results[i]
#         if team[1] > maxteam[1]:
#             maxteam = team
#         elif team[1] == maxteam[1] and team[0] < maxteam[0]:
#             maxteam = team
#             results.remove(maxteam)
#         table.append(maxteam)
# for team in table:
#     print(f'{team[0]}:{team[1]}')


# ===========================================================================


# ans = {}
# for i in range(8):
#     team = input().split(',')
#     ans[team[0]] = len(team) - 1

# team_dict = {}
# for key, value in ans.items():
#     if value in team_dict:
#         team_dict[value].append(key)
#     else:
#         team_dict[value] = [key]

# for point in team_dict:
#     team_dict[point] = sorted(team_dict[point])

# # Sort the wins in descending order
# sorted_wins = sorted(team_dict.keys(), reverse=True)

# for wins in sorted_wins:
#     team_list = team_dict[wins]
#     for team in sorted(team_list):
#         print(f"{team}:{wins}")


# # Initialize a dictionary to store the number of wins for each team
# wins = {}

# # Input the data and calculate the wins for each team
# for i in range(8):
#     team_data = input().split(',')
#     wins[team_data[0]] = len(team_data) - 1

# # Create a dictionary to group teams with the same number of wins
# teams_by_wins = {}
# for team, num_wins in wins.items():
#     if num_wins in teams_by_wins:
#         teams_by_wins[num_wins].append(team)
#     else:
#         teams_by_wins[num_wins] = [team]

# # Sort the wins in descending order and teams in alphabetical order
# sorted_wins = sorted(teams_by_wins.items(), key=lambda x: (-x[0], x[1]))

# # Print the IPL points table in the desired format
# for wins, team_list in sorted_wins:
#     for team in team_list:
#         print(f"{team}:{wins}")



ipl = {}
for i in range(8):
    team = input().split(',')
    ipl[team[0]] = len(team)-1

sort_ipl = {}
for key, value in ipl.items():
    if value in sort_ipl:
        sort_ipl[value].append(key)
    else:
        sort_ipl[value] = [key]

for point in sort_ipl:
    sort_ipl[point] = sorted(sort_ipl[point])

sort_point = sorted(sort_ipl.keys(),reverse=True)
# sort_point = sorted(sort_ipl.keys())

for point in sort_point:
    team_list = sort_ipl[point]
    for team in team_list:
        print(f"{team}:{point}")

print()
print(ipl)
print(sort_ipl)