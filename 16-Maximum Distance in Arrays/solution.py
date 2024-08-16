class Solution:
    def maxDistance(self, arrays):
        mn = arrays[0][0]
        mx = arrays[0][-1]
        res = 0

        for i in range(1, len(arrays)):
            arr = arrays[i]
            res = max(res, abs(arr[-1] - mn), abs(mx - arr[0]))
            mn = min(mn, arr[0])
            mx = max(mx, arr[-1])

        return res