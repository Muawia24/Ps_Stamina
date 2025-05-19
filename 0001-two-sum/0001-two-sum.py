class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i in range(len(nums)):
            sec_num = target - nums[i]
            if sec_num in num_map:
                return [num_map[sec_num], i]
            num_map[nums[i]] = i
        