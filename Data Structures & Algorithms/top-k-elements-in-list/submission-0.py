class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # loop through the numbers and count how many of each
        # return the k most frequent numbers
        # [3, 4, 5, 2, 1, 1] k = 2 output would be [x, 1]
        map = defaultdict(int)
        for num in nums:
            map[num] += 1
                
        return heapq.nlargest(k, map, key=map.get)
