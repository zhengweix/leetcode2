from heapq import *
class Solution:
    '''
    You have some sticks with positive integer lengths.
    You can connect any two sticks of lengths X and Y into one stick by paying a cost of X + Y.  You perform this action until there is one stick remaining.
    Return the minimum cost of connecting all the given sticks into one stick in this way.

    Example 1:
    Input: sticks = [2,4,3]
    Output: 14
    Explanation: You start with sticks = [2,4,3].
    1. Combine sticks 2 and 3 for a cost of 2 + 3 = 5. Now you have sticks = [5,4].
    2. Combine sticks 5 and 4 for a cost of 5 + 4 = 9. Now you have sticks = [9].
    There is only one stick left, so you are done. The total cost is 5 + 9 = 14.

    Example 2:
    Input: sticks = [1,8,3,5]
    Output: 30
    Explanation: You start with sticks = [1,8,3,5].
    1. Combine sticks 1 and 3 for a cost of 1 + 3 = 4. Now you have sticks = [4,8,5].
    2. Combine sticks 4 and 5 for a cost of 4 + 5 = 9. Now you have sticks = [9,8].
    3. Combine sticks 9 and 8 for a cost of 9 + 8 = 17. Now you have sticks = [17].
    There is only one stick left, so you are done. The total cost is 4 + 9 + 17 = 30.

    Example 3:
    Input: sticks = [5]
    Output: 0
    Explanation: There is only one stick, so you don't need to do anything. The total cost is 0.

    Greedy, Array, Heap (Priority Queue)
    Minimum Cost to Merge Stones
    '''
    def connectSticks(self, sticks):
        ans = 0
        heapify(sticks)
        while len(sticks) > 1:
            s = heappop(sticks) + heappop(sticks)
            ans += s
            heappush(sticks, s)
        return ans

    def main(self):
        print(self.connectSticks([1,8,3,5]))

S = Solution()
S.main()