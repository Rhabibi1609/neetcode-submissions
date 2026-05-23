class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        sol = {}
        for i,n in enumerate(nums):
            complement = target - n

            if complement in sol:

                return [sol[complement],i]

            sol[n] = i
        