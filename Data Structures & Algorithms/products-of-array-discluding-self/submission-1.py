class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # same size array
        # need to skip the current part of the array
        #was thinking of doing slice of the array, but it breaks down when you get to the second index
        # looping through with an outer loop, then inner loop would skip the current outer loop index, multiply and save the result into a new array
        # O(n^2 time)
        # graph would not work because we are not ordering
        # hashmap will not work because you can't access the value without using an outer loop resulting in n^2
        # stack does not help because ordering does not really matter
        #sorting algorithms don't help with the sorting 
        #prefix = [1, 2, 8, 48]
        #suffix = [48, 48, 24, 6]
        prefix = [nums[0]] + [0] * (len(nums) - 1)
        suffix = [0] * (len(nums) - 1) + [nums[len(nums) - 1]]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] *  nums[i]

        for i in range(len(nums) - 2, 0, -1):
            suffix[i] = suffix[i + 1] * nums[i]
        
        res = [0] * len(nums)
        for i in range(0, len(nums)):
            if i == 0:
                res[i] = 1 * suffix[i + 1]
            elif i == len(nums) - 1:
                res[i] = prefix[i - 1] * 1
            else:
                res[i] = prefix[i - 1] * suffix[i + 1]
        #res = [48, 24, 12, 8]
        return res
