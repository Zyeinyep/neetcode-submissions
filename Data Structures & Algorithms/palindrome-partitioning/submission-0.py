class Solution:
    def partition(self, s: str) -> List[List[str]]:
        part = []
        def backtrack(path, start):
            if start == len(s):
                part.append(path[:])
                return
            for i in range(start,len(s)):
                curr = s[start:i+1]
                if curr == curr[::-1]:
                    path.append(curr)
                    backtrack(path,i+1)
                    path.pop()

        backtrack([],0)
        return part
        
        