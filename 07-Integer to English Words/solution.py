class Solution:
    def numberToWords(self, num):
        if num == 0:
            return "Zero"
        
        largeDenominations = ["Thousand", "Million", "Billion"]
        res = self.helper(num % 1000)
        num //= 1000

        for i in range(len(largeDenominations)):
            if num > 0 and num % 1000 > 0:
                res = self.helper(num % 1000) + largeDenominations[i]
            num //= 1000

        return res.strip()
    
    def helper(self, num):
        digitString = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        teenString = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tenString = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        
        res = ""
        if num > 99:
            res += digitString[num // 100] + " Hundred "

        num %= 100
        if num < 20 and num > 9:
            res += teenString[num - 10] + " "
        else:
            if num >= 20:
                res += tenString[num // 10] + " "
            num %= 10
            if num > 0:
                res += digitString[num] + " "
        
        return res