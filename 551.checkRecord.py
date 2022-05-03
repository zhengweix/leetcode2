class Solution:
    def checkRecord(self, s: str) -> bool:
        if 'LLL' in s:
            return False

        rec = 0
        for r in s:
            if r == 'A':
                rec += 1
                if rec > 1:
                    return False

        return True
#552