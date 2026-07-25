class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [0]*(len(nums2))
        stack = []

        for i in range(len(nums2)-1, -1,-1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1]
            else:
                res[i] = -1
            stack.append(nums2[i])
        ans = []
        for n in nums1:
            for i,e in enumerate(nums2):
                if n == e:
                    ans.append(res[i])
        return ans



        
        