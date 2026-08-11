class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        m = max(arr)
        for i,e in enumerate(arr):
            if e < m:
                arr[i] = m
            else:
                if i == len(arr) - 1:
                    arr[i] = -1
                    continue
                m = max(arr[i+1:])
                arr[i] = m
        return arr
        