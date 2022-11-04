import re
class Solution:
    '''
    Given an alphanumeric string, extract maximum numeric value from that string. Alphabets will only be in lower case.
    One approach to solving the problem is discussed here, other using Regular expressions is given in Set 2
    Examples:
    Input : 100klh564abc365bg
    Output : 564
    Maximum numeric value among 100, 564 and 365 is 564.
    Input : abchsd0sdhs
    Output : 0
    '''
    @staticmethod
    def extractMaximum(s):
        ans, num = 0, ''
        for c in s:
            if c.isdigit():
                num += c
            else:
                if num:
                    ans = max(int(num), ans)
                num = ''
        if num:
            ans = max(int(num), ans)
        return ans

    @staticmethod
    def extractMaximum1(s):
        return max([int(x) for x in re.findall('\d+', s)])

print(Solution.extractMaximum1('100klh564abc365bg'))
        