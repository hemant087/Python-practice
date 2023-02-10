# # def fun(n):
# #     if n==0:
# #         return
# #     fun(n-1)
# #     print(n)
# #     return
# #
# #
# # fun(11)


# def fun(n):
#     if n==1 or n==2:
#         return 1
#     return(fun(n-1)+fun(n-2))

# print(fun(1000))

def isSorted(a):
    l = len(a)
    if l == 0 or l == 1:
        return True
    if a[0] > a[1]:
        return False
    subSet = a[1:]
    isSorted(subSet)
    if subSet:
        return True
    else:
        return False


a = {1, 2, 3, 4, 5, 6}
isSorted(a)
