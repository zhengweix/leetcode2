class Solution:
    '''
    Given a positive integer n, find and return the longest distance between any two adjacent 1's in the binary representation of n. If there are no two adjacent 1's, return 0.
    Two 1's are adjacent if there are only 0's separating them (possibly no 0's). The distance between two 1's is the absolute difference between their bit positions. For example, the two 1's in "1001" have a distance of 3.

    Example 1:
    Input: n = 22
    Output: 2
    Explanation: 22 in binary is "10110".
    The first adjacent pair of 1's is "10110" with a distance of 2.
    The second adjacent pair of 1's is "10110" with a distance of 1.
    The answer is the largest of these two distances, which is 2.
    Note that "10110" is not a valid pair since there is a 1 separating the two 1's underlined.

    Example 2:
    Input: n = 8
    Output: 0
    Explanation: 8 in binary is "1000".
    There are not any adjacent pairs of 1's in the binary representation of 8, so we return 0.

    Example 3:
    Input: n = 5
    Output: 2
    Explanation: 5 in binary is "101".

    Bit Manipulation

    1707. Maximum XOR With an Element From Array
    1178. Number of Valid Words for Each Puzzle
    1542. Find Longest Awesome Substring

    progressively check the bits from right to left e.g. for number 22 in binary format (0b10110), 0-1-1-0-1 are progressively checked.
    If the current bit is 1 and 1 has appeared before, the distance is compared against the current max and update if larger.
    Update the position of previous 1 to the current position.
    If the current bit is 0, move to next bit and increase current gap by one.
    '''
    @staticmethod
    def binaryGap(n):
        ans = 0
        n = str(bin(n)[2:])
        for i in range(len(n)-1):
            if n[i] == '1':
                for j in range(i+1, len(n)):
                    if n[j] == '1':
                        ans = max(ans, j-i)
                        break
        return ans

    @staticmethod
    def binaryGap1(n):
        ans, i, one = 0, 0, None
        while n:
            if n & 1: #current bit is one
                if one is not None:
                    ans = max(ans, i - one)  #one has appeared before
                one = i
            i += 1
            n >>= 1 #left shift one bit
        return ans

print(Solution.binaryGap1(22))