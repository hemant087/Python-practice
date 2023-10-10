# nums = [8,1,2,2,3]
# # nums.sort()
# dct = {}

# for i in range(len(nums)):
#     if nums[i] not in dct:
#         dct[nums[i]] = i
# ans = []
# for i in nums:
#     ans.append(dct[i])
# print(ans)


# _______________________________________________________________________


class Solution:

    def fect(self, num):
        temp = 1
        while num > 1:
            temp *= num
            num -= 1
        return temp

    def nPr(self, n, r):
        return self.fect(n)/self.fect(n-r)


ans = Solutio