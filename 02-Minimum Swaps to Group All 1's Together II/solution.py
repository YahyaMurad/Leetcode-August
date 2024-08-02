class Solution:
    def minSwaps(self, nums):
        total = sum(nums)
        res = count = sum(nums[:total])

        for i in range(total, len(nums) + total):
            count += nums[i % len(nums)]
            count -= nums[(i - total + len(nums)) % len(nums)]
            res = max(res, count)

        return total - res
