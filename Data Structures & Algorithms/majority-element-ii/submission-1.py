class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1 = 0
        cand2 = 0 
        count1 = 0
        count2 = 0
        for e in nums:
            if count1 == 0:
                cand1 = e
            if count2 == 0:
                cand2 = e
            if e == cand1:
                count1 += 1
            elif e == cand2:
                count2 += 1
            else:
                count1 -=1
                count2 -=1
        count1 =0 
        count2 =0
        for num in nums:
            if num == cand1:
                 count1 += 1
            elif num == cand2:
                count2 += 1
        result = []

        if count1 > len(nums)//3:
            result.append(cand1)
        
        if count2 > len(nums)//3 and cand1 != cand2:
            result.append(cand2)
            
        return result


        