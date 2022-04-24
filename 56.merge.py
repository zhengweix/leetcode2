class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals_ = []
        if not intervals:
            return intervals_
        intervals.sort(key=lambda x: x[0])
        current = intervals[0]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] <= current[1]:
                current = [current[0], max(interval[1], current[1])]
            else:
                intervals_.append(current)
                current = interval

        intervals_.append(current)
        return intervals_