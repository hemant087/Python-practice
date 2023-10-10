# file = open("hemant.txt","w")
# file.write("Hi!")
# file.writelines(L) for L = {}

# import csv
# with open('data.csv','r') as file:
#     # line = file.readlines()
#     for i in range(10):
#         data =[file.readline().split(',')]
#         print(data)
# print(line[:5])

# data = csv.reader(file)
# # print(data)
# for row in data:
#     print(row)

# /===================================================================


# def write_AP(a_1, d, n):
#     ans = a_1
#     with open('out.txt', 'w') as file:
#         # file.writelines(str(a_1))
#         for i in range(n):
#             file.write(str(ans) + '\n')  # Add newline character
#             ans += d
#     return 'out.txt'


# print(write_AP(1, 3, 5))


# ============================================================


# def add_period(filename):
#     with open(filename, "r") as file:

#         with open('out.txt', 'w') as file2:
#             line = file.readline()
#             while line:
#                 file2.write(str(line.strip()) +'.'+'\n')
#                 line = file.readline()

#     return "out.txt"


# add_period('file.txt')
# ====================================================================

with open('gate24.txt','r') as file:
    line = file.readline()
    while line:
        line.split(',')
        print(line)
        line = file.readline()