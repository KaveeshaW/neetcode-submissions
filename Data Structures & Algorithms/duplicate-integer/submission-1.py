class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = {}
        for num in nums:
            if num in numbers:
                numbers[num] += 1
            if num not in numbers:
                numbers[num] = 1
        return any(number > 1 for number in numbers.values())