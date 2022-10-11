class Solution:
    '''
    There is an infinite array of integers numbered consecutively from 0. At each step, a pointer can move from index i to index i+j, or remain where it is. The value of i begins at 0. The value of j begins at 1 and at each step, jincrements by 1. There is one known index that must be avoided.
    Determine the highest index that can be reached in a given number of steps

    Example
    steps = 4
    badElement = 6
    Explanation:
    The pointer is limited to 4 steps and should avoid the bad item 6
    j = 1
    Scenario 1:
    Step 1: move = 1, i = 0, j = 2
    Step 2: move = 2, i = 1, j = 3
    Step 3: move = 0, i = 3, j = 4, i + move = 6
    Step 4: move = 4, i = 7, j = 5

    Scenario 2:
    Step 1: move = 0, i = 0, j = 2
    Step 2: move = 2, i = 2, j = 3
    Step 3: move = 3, i = 5, j = 4
    Step 4: move = 4, i = 9, j = 5
    '''
    def minIndex(self, steps, badElement):
        i, j, = 0, 1
        for s in range(steps):
            #! https://www.geeksforgeeks.org/maximum-index-a-pointer-can-reach-in-n-steps-by-avoiding-a-given-index-b/
            if i + j != badElement:
                i += j
            j += 1


    def main(self):
        print(self.minIndex(3, 2))

S = Solution()
S.main()
