import itertools
class Solution:
    def largestTimeFromDigits(self, arr: list) -> str:
        output = ''
        limit = diff = 2359
        limits = [23, 59]
        digits = []
        for a in list(itertools.permutations(arr)):
            t = int(self.stringFormat(a))
            if t > limit or int(''.join([str(a[0]), str(a[1])])) > limits[0] or int(''.join([str(a[2]), str(a[3])])) > limits[1]:
                continue

            if limit - t <= diff:
                diff = limit - t
                digits = a

        if not digits:
            return ''

        for i in range(4):
            output += str(digits[i])
            if i == 1:
                output += ':'

        return output

    def stringFormat(self, arr: list) -> str:
        return ''.join([str(a) for a in arr])
