from collections import *
class Solution:
    '''
    A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID.
    Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, manager[headID] = -1. Also, it is guaranteed that the subordination relationships have a tree structure.
    The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.
    The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).
    Return the number of minutes needed to inform all the employees about the urgent news.

    Example 1:
    Input: n = 1, headID = 0, manager = [-1], informTime = [0]
    Output: 0
    Explanation: The head of the company is the only employee in the company.

    Example 2:
    Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
    Output: 1
    Explanation: The head of the company with id = 2 is the direct manager of all the employees in the company and needs 1 minute to inform them all.
    The tree structure of the employees in the company is shown.

    Constraints:
    1 <= n <= 105
    0 <= headID < n
    manager.length == n
    0 <= manager[i] < n
    manager[headID] == -1
    informTime.length == n
    0 <= informTime[i] <= 1000
    informTime[i] == 0 if employee i has no subordinates.
    It is guaranteed that all the employees can be informed.

    Tree, Depth-First Search, Breadth-First Search

    Verify Preorder Serialization of a Binary Tree, Most Frequent Subtree Sum, Pseudo-Palindromic Paths in a Binary Tree
    '''
    def numOfMinutes(self, n, headID, manager, informTime):
        tree = defaultdict(list)
        for i in range(n):
            tree[manager[i]].append(i)
        ans, queue = 0, [(headID, informTime[headID])]
        while queue:
            u, t = queue.pop(0)
            ans = max(ans, t)
            for v in tree[u]:
                queue.append((v, t + informTime[v]))
        return ans

    def numOfMinutes1(self, n, headID, manager, informTime):
        tree = defaultdict(list)
        for i in range(n):
            tree[manager[i]].append(i)

        def helper(u, time):
            nonlocal ans
            if u not in tree:
                return 0

            for v in tree[u]:
                ans = max(ans, time[u] + informTime[v])
                time[v] = time[u] + informTime[v]
                helper(v, time)

        ans = 0
        helper(headID, {headID: informTime[headID]})
        return ans


    def main(self):
        print(self.numOfMinutes1(10, 3, [8,9,8,-1,7,1,2,0,3,0], [224,943,160,909,0,0,0,643,867,722]))

S = Solution()
S.main()