
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # Two-pass Hash Table
        # dic = {}
        # for i in range(len(nums)):
        #     dic[nums[i]] = i
        # for i in range(len(nums)):
        #     if target - nums[i] in dic and dic[target - nums[i]] != i:
        #         return [i, dic[target - nums[i]]]

        # One-pass Hash Table
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] in dict:
                return [dict[target - nums[i]], i]
            dict[nums[i]] = i
        return None