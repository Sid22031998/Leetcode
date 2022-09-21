class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # Brute Force: Accepted, TC: O(len(nums1)*len(nums2))
        # ans=[-1]*len(nums1)
        # for i in range(len(nums1)):
        #     index=nums2.index(nums1[i])
        #     for j in range(index+1, len(nums2)):
        #         if nums2[j]>nums1[i]:
        #             ans[i]=nums2[j]
        #             break
        # return ans
    
        # Optimised using stack and hash map, TC: O(len(nums1) + len(nums2))
        n=len(nums1)
        m=len(nums2)
        ans=[-1]*n
        d={}
        for i in range(n):
            d[nums1[i]]=i
        stack=[]
        for i in range(m-1,-1,-1):
            while len(stack) and stack[-1]<=nums2[i]:
                stack.pop()
            if nums2[i] in d:
                if len(stack):
                    ans[d[nums2[i]]]=stack[-1]
            stack.append(nums2[i])
        return ans
            
