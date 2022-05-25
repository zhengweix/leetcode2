from heapq import *
class MedianFinder:
    '''
    The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

    For example, for arr = [2,3,4], the median is 3.
    For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
    Implement the MedianFinder class:

    MedianFinder() initializes the MedianFinder object.
    void addNum(int num) adds the integer num from the data stream to the data structure.
    double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

    Input
    ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
    [[], [1], [2], [], [3], []]
    Output
    [null, null, null, 1.5, null, 2.0]

    Explanation
    MedianFinder medianFinder = new MedianFinder();
    medianFinder.addNum(1);    // arr = [1]
    medianFinder.addNum(2);    // arr = [1, 2]
    medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
    medianFinder.addNum(3);    // arr[1, 2, 3]
    medianFinder.findMedian(); // return 2.0

    Constraints:
    -105 <= num <= 105
    There will be at least one element in the data structure before calling findMedian.
    At most 5 * 104 calls will be made to addNum and findMedian.

    Follow up:
    If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
    If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
    '''
    def __init__(self):
        self.smallNums = []
        self.largeNums = []

    def addNum(self, num: int) -> None:
        if not self.smallNums or -self.smallNums[0] >= num:
            heappush(self.smallNums, -num)
        else:
            heappush(self.smallNums, num)

        lenSmall = len(self.smallNums)
        lenLarge = len(self.largeNums)
        if lenLarge > lenSmall:
            heappush(self.smallNums, -heappop(self.largeNums))
        elif lenSmall > lenLarge + 1:
            heappush(self.largeNums, -heappop(self.smallNums))

    def findMedian(self) -> float:
        if len(self.smallNums) == len(self.largeNums):
            return (-self.smallNums[0]+self.largeNums[0])/2.0
        else:
            return -self.smallNums[0]/1.0



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

