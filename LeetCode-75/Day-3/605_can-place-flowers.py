  class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        c= 0
        a = len(flowerbed)
        for i in range(a):
            if flowerbed[i] == 0:
                left = (i == 0) or (flowerbed[i-1] == 0)
                right = (i == a-1) or (flowerbed[i+1] == 0)
                if left and right:
                    flowerbed[i] = 1
                    c += 1
        return c >= n
