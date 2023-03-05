from string import ascii_lowercase
class Solution:
    '''
    A palindrome is a word, which reads the same backward as forward. Some examples of palindromes are: "kayak", "radar", "mom".
    Write a function: class Solution { public String solution (int N, int K); }
    that, given two integers N and K, returns a palindrome of length N which consists of K distinct lower-case letters (a-z).

    Examples:
    1. Given N = 5, K = 2, your function may return "abbba". There are many other possibilities; for example, it could also return "zdzdz". On the other hand, "aaaaa" is an incorrect answer as it contains only one distinct letter.

    2. Given N= 8, K = 3, your function may return "ppsccspp".
    3. Given N= 3, K = 2, your function may return "opo".

    Assume that:
    N is an integer within the range [1..200];
    K is an integer within the range [1..26];
    Creation of the required palindrome is always possible.
    '''
    @staticmethod
    def distinctPalindrome(n, k):
        mp, mid, i = list(ascii_lowercase), n >> 1, 0
        if n % 2:
            ans = mp[i]
        else:
            ans = mp[i] + mp[i]
            mid -= 1
        i += 1
        for _ in range(mid):
            c = mp[i % k]
            ans = c + ans + c
            i += 1
        return ans

print(Solution.distinctPalindrome1(8, 3))