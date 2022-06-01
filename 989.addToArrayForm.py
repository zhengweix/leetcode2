class Solution:
    '''
    The array-form of an integer num is an array representing its digits in left to right order.
    For example, for num = 1321, the array form is [1,3,2,1].
    Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

    Input: num = [1,2,0,0], k = 34
    Output: [1,2,3,4]
    Explanation: 1200 + 34 = 1234

    Input: num = [2,7,4], k = 181
    Output: [4,5,5]
    Explanation: 274 + 181 = 455

    Input: num = [2,1,5], k = 806
    Output: [1,0,2,1]
    Explanation: 215 + 806 = 1021

    Constraints:
    1 <= num.length <= 104
    0 <= num[i] <= 9
    num does not contain any leading zeros except for the zero itself.
    1 <= k <= 104
    '''
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        sk = str(k)
        lnum, lk = len(num), len(sk)
        n = max(lnum, lk)
        carry = 0
        for i in range(1, n + 1):
            if i > lnum:
                sum = int(sk[-i]) + carry
                num = [sum % 10] + num
            else:
                if i > lk:
                    sum = num[-i] + carry
                else:
                    sum = num[-i] + int(sk[-i]) + carry
                num[-i] = sum % 10
            carry = sum // 10
        if carry > 0:
            return [1] + num
        return num

    def addToArrayForm1(self, num: List[int], k: int) -> List[int]:
        for i in range(len(num) - 1, -1, -1):
            sum = num[i] + k
            num[i] = sum % 10
            k = sum // 10
        while k > 0:
            num = [k % 10] + num
            k //= 10
        return num

#247 462 1429