class Solution:
    '''
    Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],…] (si < ei), find the minimum number of conference rooms required.

    Example 1:
    Input: [[0, 30],[5, 10],[15, 20]]
    Output: 2

    Example 2:
    Input: [[7,10],[2,4]]
    Output: 1

    Related Topics
    Heap, Greedy, Sort
    '''
    def minMeetingRooms(self, intervals):
        n = len(intervals)
        if n == 1:
            return n
        intervals.sort(key=lambda x: x[0])
        ends = [intervals[0][1]]
        for i in range(1, n):
            itvl = intervals[i]
            for end in ends:
                if end <= itvl[0]:
                    break
            else:
                ends.append(itvl[1])
        return len(ends)

    def main(self):
        print(self.minMeetingRooms([[0, 30],[5, 10],[15, 20]]))

S = Solution()
S.main()