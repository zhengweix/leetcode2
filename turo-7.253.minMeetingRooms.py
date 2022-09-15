from heapq import *
class Solution:
    '''
    Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],…] (si < ei), find the minimum number of conference rooms required.

    Example 1:
    Input: [[0, 30],[5, 10],[15, 20]]
    Output: 2

    Example 2:
    Input: [[7,10],[2,4]]
    Output: 1

    Related Topics:
    Heap, Greedy, Sort

    Next challenges:
    56 252 452 1094
    '''
    #? keywords: time intervals, minimum number
    #? approach: heap to store and retrieve endtimes, greedy to update endtime
    # input: [[0, 30],[5, 10],[15, 20]]
    # output: 2
    # tc: O(nlogn) sc: O(n)
    def minMeetingRooms(self, intervals):
        intervals.sort(key=lambda x:x[0])
        minHeap = [intervals[0][1]]
        ans = 1
        for itvl in intervals[1:]:
            start, end = itvl
            if start < minHeap[0]:
                ans += 1
                heappush(minHeap, end)
            else:
                heappop(minHeap)
                heappush(minHeap, end)
        return ans


    def main(self):
        print(self.minMeetingRooms([[9,10],[4,9],[4,17]]))

S = Solution()
S.main()