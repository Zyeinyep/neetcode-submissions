class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for i in logs:
            if i[0] != ".":
                count +=1
            elif i[1] == ".":
                if count >0 :
                    count -=1
        return count

        