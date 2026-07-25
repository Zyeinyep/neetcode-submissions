class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        best = max(arr)
        for i,e  in enumerate(arr):
            if e < best:
                arr[i] = best
            else:
                if i < len(arr) - 1:
                    best = max(arr[i+1:])
                else:
                    best = -1
                arr[i] = best
        return arr


        