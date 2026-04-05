class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        d = {}
        for num in nums2[::-1]:
            while stack and stack[-1] < num:
                stack.pop()
            
            if stack:
                d[num] = stack[-1]
            stack.append(num)
        return [d.get(num, -1) for num in nums1]
