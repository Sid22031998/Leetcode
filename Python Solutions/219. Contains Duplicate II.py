class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        duplicates={}
        n=len(nums)
        for i in range(n):
            if nums[i] in duplicates:
                if abs(duplicates[nums[i]]-i)<=k:
                    return True
            # will store the last index value
            duplicates[nums[i]]=i
        return False
