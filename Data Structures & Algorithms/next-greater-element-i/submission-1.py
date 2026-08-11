class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d= {}
        stack=[]
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                d[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        for i,e in enumerate(nums1):
            nums1[i] = d.get(e,-1)
        return nums1
        
        