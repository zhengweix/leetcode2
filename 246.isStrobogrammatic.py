class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        dict = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        tmp = ''
        for i in num:
            if i not in dict:
                return False
            tmp += num[i]

        return tmp[::-1] == num