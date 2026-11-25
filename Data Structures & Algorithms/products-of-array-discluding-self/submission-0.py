class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1]* n
        right = [1] * n
        # left:從左往右
        for i in range(1,n):
            # left[i] = left[i-1] * nums[i-1]
            left[i] = left[i-1]*nums[i-1]
        # rigt 從右往左 倒著走
        for i in range(n-2,-1,-1):
            right[i] = right[i+1]*nums[i+1]
        return [left[i] * right[i] for i in range(n)]