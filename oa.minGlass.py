class Solution:
    '''
    There are N empty glasses with a capacity of 1, 2, ..., N liters (there is exactly one glass of each unique capacity). You want to pour exactly K liters of water into glasses. Each glass may be either full or empty (a glass cannot be partially filled). What is the minimum number of glasses that you need to contain K liters of water?
    Write a function: class Solution public int solution (int N, int K); }
    that, given two integers N and K, returns the minimum number of glasses that are needed to contain exactly K liters of water. If it is not possible to pour exactly K liters of water into glasses then the function should return -1.

    Examples:
    1. Given N = 5 and K = 8, the function should return 2. There are five glasses of capacity 1, 2, 3, 4 and 5. You can use two glasses with capacity 3 and 5 to hold 8 liters of water.
    2. Given N= 4 and K = 10, the function should return 4. You must use all the glasses to contain 10 liters of water. 11
    3. Given N= 1 and K = 2, the function should return -1. There is only one glass with capacity 1, so you cannot pour 2 liters of water.
    4. Given N= 10 and K = 5, the function should return 1. You can use the glass with capacity 5.

    Write an efficient algorithm for the following assumptions:
    N is an integer within the range [1..1,000,000];
    K is an integer within the range [1..1,000,000,000].
    '''
    @staticmethod
    def missingNumber(N, K):
        ans = 0
        for i in range(N, 0, -1):
            if K > 0:
                ans += 1
                K -= i
        return ans if K <= 0 else -1

print(Solution.missingNumber(5, 8))
print(Solution.missingNumber(4, 10))
print(Solution.missingNumber(1, 2))
print(Solution.missingNumber(10, 5))
