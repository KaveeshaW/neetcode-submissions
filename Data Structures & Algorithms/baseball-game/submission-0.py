class Solution:
    def calPoints(self, operations: List[str]) -> int:
        results = []
        index = 0
        for operation in operations:
            if operation == '+':
                first = index - 2
                second = index - 1
                result1 = int(results[first])
                result2 = int(results[second])
                print(result1)
                print(result2)
                print(result1 + result2)
                results.append(result1 + result2)
                index += 1
            elif operation == 'D':
                previous = index - 1
                results.append(int(results[previous]) * 2)
                index += 1
            elif operation == 'C':
                results.pop()
                index -= 1
            else:
                results.append(int(operation))
                index += 1
        print(results)
        return sum(results)
        
