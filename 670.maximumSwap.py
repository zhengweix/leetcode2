class Solution:
    """
    You are given an integer num. You can swap two digits at most once to get the maximum valued number.
    Return the maximum valued number you can get.

    Example 1:
    Input: num = 2736
    Output: 7236
    Explanation: Swap the number 2 and the number 7.

    Example 2:
    Input: num = 9973
    Output: 9973
    Explanation: No swap.

    Similar Questions
    321. Create Maximum Number

    Related Topics
    Math Greedy
    """
    @staticmethod
    def maximumSwap(num):
        nums = list(map(int, str(num))) # array of digits
        ii = m = mm = None
        for i in reversed(range(len(nums))):
            # determining right swap digit
            if not m or nums[m] < nums[i]:
                m = i
            # determining left swap gigit
            if nums[i] < nums[m]:
                ii, mm = i, m
        if mm:
            nums[ii], nums[mm] = nums[mm], nums[ii]
        return int("".join(map(str, nums)))

print(Solution.maximumSwap(123456789))