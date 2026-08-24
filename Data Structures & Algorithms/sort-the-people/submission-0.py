
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i,e in enumerate(heights):
            heights[i] = (e,i)
        heights.sort(reverse=True)
        ans = []
    
        for e,i in heights:
            ans.append(names[i])
        return ans

        