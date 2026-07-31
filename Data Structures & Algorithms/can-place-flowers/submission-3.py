class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(0, len(flowerbed)):
            prev = i - 1
            if i - 1 < -1:
                prev = 0
            nexxt = i + 1
            if i+1 > len(flowerbed) - 1:
                nexxt = len(flowerbed) - 1
            if flowerbed[i] == 0 and flowerbed[nexxt] == 0 and flowerbed[prev] == 0:
                    flowerbed[i] = 1
                    count +=1
        if count >= n:
            return True
        return False


 

        