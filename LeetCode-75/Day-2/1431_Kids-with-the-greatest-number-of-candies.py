class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        n=len(candies)
        m=max(candies)
        res=[]
        for i in range (n):
            a = candies[i]+extraCandies
            b = a>=m
            res.append(b)
        return res   
