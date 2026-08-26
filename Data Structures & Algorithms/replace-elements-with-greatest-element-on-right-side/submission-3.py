class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr), 1):
                print(j)
                if(max < arr[j]):
                    max = arr[j]
            arr[i] = max
            max = 0
        final_element = len(arr) - 1
        arr[final_element] = -1
        return arr