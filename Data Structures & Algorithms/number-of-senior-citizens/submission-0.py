class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        count = 0
        for e in details:
            if int(e[11] + e[12]) > 60:
                count += 1
        return count


        