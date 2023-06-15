class Solution:
    def twoSum(self, nums: List[int], target: int):
        ans = {}
        for i in range(len(nums)):
            if target - nums[i] in ans:
                return [ans[target - nums[i]],i]
            else:
                ans[nums[i]]=i