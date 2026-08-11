class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 1:
                i = i+2
            else:
                if i+1 < len(flowerbed):
                    if flowerbed[i+1] == 1:
                        i += 3
                    else:
                        flowerbed[i] = 1
                        n -=1
                        i+=2

                else:
                    flowerbed[i] = 1
                    n -=1
                    i +=1
        return n <= 0
        
