class Solution:
    def reorderSpaces(self, text: str) -> str:
        lspace = text.count(' ')
        text1 = text.lstrip()
        text1 = text1.rstrip()
        words = re.split(" +", text1)
        lwords = len(words)
        if lwords == 1:
            return words[0] + ' ' * lspace
        nspace = lspace // (lwords - 1)
        rspace = lspace % (lwords - 1)
        text = (' ' * nspace).join(words)
        if rspace != 0:
            text += ' ' * rspace
        return text