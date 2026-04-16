class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        newStart, newEnd = newInterval

        for s, e in intervals:
            if e < newStart:
                # current interval is completely before newInterval
                result.append([s, e])
            elif s > newEnd:
                # current interval is completely after newInterval
                result.append([newStart, newEnd])
                newStart, newEnd = s, e
            else:
                # overlap, so merge into newInterval
                newStart = min(newStart, s)
                newEnd = max(newEnd, e)

        result.append([newStart, newEnd])
        return result

            

        