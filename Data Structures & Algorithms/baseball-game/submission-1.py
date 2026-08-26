from collections import deque
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for op in operations:
            print(record)
            if op not in 'D+C':
                record.append(int(op))
            else:
                if op == '+':
                    record.append(record[-1] + record[-2])
                elif op == 'C':
                    record.pop()
                else:
                    record.append(record[-1] * 2)
        
        return sum(record)