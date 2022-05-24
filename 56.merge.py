class Solution:
    '''
    Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

    Input: intervals = [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.
    '''

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key=lambda x: x[0])
        current = intervals[0]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] <= current[1]:
                current = [current[0], max(interval[1], current[1])]
            else:
                result.append(current)
                current = interval

        result.append(current)
        return result
#495 57 253 616 763 986