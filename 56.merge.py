class Solution:
    '''
    Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

    Input: intervals = [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.

    Constraints:
    1 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 104

    Insert Interval, Meeting Rooms, Meeting Rooms II, Teemo Attacking, Add Bold Tag in String, Range Module, Employee Free Time, Partition Labels, Interval List Intersections, Amount of New Area Painted Each Day, Longest Substring of One Repeating Character, Count Integers in Intervals, Divide Intervals Into Minimum Number of Groups
    '''
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            itvl = intervals[i]
            if itvl[0] <= end:
                end = max(end, itvl[1])
                ans[-1] = [ans[-1][0], end]
            else:
                ans.append(itvl)
                end = itvl[1]
        return ans

    def main(self):
        print(self.merge([[1,3],[2,6],[8,10],[15,18]]))

S = Solution()
S.main()