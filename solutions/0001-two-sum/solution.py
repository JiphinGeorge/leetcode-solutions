class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i in range(len(nums)):
            visited[nums[i]] = i
        
        for i in range(len(nums)): #O(n)
            rem = target - nums[i]
            if rem in visited and i != visited[rem]: #~O(1)
                return[visited[rem], i]

