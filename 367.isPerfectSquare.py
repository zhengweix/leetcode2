class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        i = math.floor(num/2)
        while i**2 > num:
            i = math.floor((i+num/i)/2)

        return i**2 == num