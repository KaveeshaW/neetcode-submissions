class Solution:
    def sortColors(self, nums: List[int]) -> None:
        colors = [0] * 3
        for n in nums:
            colors[n] += 1
        print(colors)
        index = 0

        # go through the list
        for color in range(len(colors)):
            for _ in range(colors[color]):
                # print(k)
                nums[index] = color
                index += 1
