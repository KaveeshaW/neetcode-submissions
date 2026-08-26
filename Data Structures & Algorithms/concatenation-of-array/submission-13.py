class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * 2 * len(nums)
        print(ans)
        j = len(nums)
        for index, num in enumerate(nums):
            ans[index] = nums[index]
            ans[index + j] = nums[index]
        return ans
        # for num in nums:
        #     nums.append(num)
        # return nums