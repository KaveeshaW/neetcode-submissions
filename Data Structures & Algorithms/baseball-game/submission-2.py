class Solution:
    def calPoints(self, operations: List[str]) -> int:
        results = []
        for operation in operations:
            if operation == '+':
                results.append(results[-1] + results[-2])
            elif operation == 'D':
                results.append(results[-1] * 2)
            elif operation == 'C':
                results.pop()
            else:
                results.append(int(operation))
        return sum(results)
        
