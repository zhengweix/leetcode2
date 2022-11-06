from functools import *
class Solution:
    '''
    A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.
    For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
    Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

    Example 1:
    Input: s = "25525511135"
    Output: ["255.255.11.135","255.255.111.35"]

    Example 2:
    Input: s = "0000"
    Output: ["0.0.0.0"]

    Example 3:
    Input: s = "101023"
    Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

    Constraints:
    1 <= s.length <= 20
    s consists of digits only.

    String, Backtracking
    IP to CIDR
    verkada
    '''
    # tc: O(n^2), sc: O(1)
    @staticmethod
    def restoreIpAddresses(s):
        def helper(combo, i, j):
            if i == 4 and j == len(s):
                ans.append('.'.join(combo))
                return
            if j == len(s):
                return
            for k in range(j+1, min(j+4, len(s)+1)):
                if s[j] == '0' and k > j+1:
                    continue
                if int(s[j:k]) <= 255:
                    helper(combo+[s[j:k]], i+1, k)
        ans = []
        helper([], 0, 0)
        return ans
    @staticmethod
    def restoreIpAddresses1(s):
        @lru_cache(None)
        def helper(i, n):
            '''Return valid IP address for s[i:] of n groups'''
            if not n <= len(s) - i <= 3 * n:
                return []
            if i == len(s):
                return ['']
            ans = []
            k = i + 1 if s[i] == "0" else i + 3
            for j in range(i + 1, min(k + 1, len(s) + 1)):
                if j == i + 3 and s[i:j] > "255": continue
                ans.extend(".".join((s[i:j], x)) if x else s[i:j] for x in helper(j, n - 1))
            return ans

        return helper(0, 4)

print(Solution.restoreIpAddresses1('25525511135'))