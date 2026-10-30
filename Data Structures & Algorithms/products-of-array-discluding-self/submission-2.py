class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        prefix = 1

        for i in range(0, len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # orig [1, 2, 4, 6]
        # pref 48
        # res [1, 1, 2, 8]
        
        suffix = 1

        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * suffix
            suffix = suffix * nums[i]

        # suffix = 48
        #res = [48, 24, 12, 8]
        return res
