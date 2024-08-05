class Solution:
    def kthDistinct(self, arr, k):
        h = {}
        for i in arr:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1

        res = []
        for i in arr:
            if h[i] == 1:
                res.append(i)
        
        return res[k - 1] if k - 1 < len(res) else ""