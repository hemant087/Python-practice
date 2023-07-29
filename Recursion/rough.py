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


ans = Solution()
print(ans.nPr(5, 2))


class Solution:
    def fect(self, num):
        # Compute factorial of num
        factorial = 1
        while num > 1:
            factorial *= num
            num -= 1
        return factorial

    def nPr(self, n, r):
        # Compute nPr using factorials
        # numerator = self.fect(n)
        # denominator = self.fect(n-r)
        # return numerator / denominator
        return self.fect(n) / self.fect(n-r)


# Create an instance of the Solution class and call the nPr method
ans = Solution()
print(ans.nPr(5, 2))  # Should print 20
