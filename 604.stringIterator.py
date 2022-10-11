class StringIterator:
    '''
    Design and implement a data structure for a compressed string iterator. It should support the following operations: next and hasNext.
    The given compressed string will be in the form of each letter followed by a positive integer representing the number of this letter existing in the original uncompressed string.
    next() - if the original string still has uncompressed curacters, return the next letter; Otherwise return a white space.
    hasNext() - Judge whether there is any letter needs to be uncompressed.
    Example:
    StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");
    iterator.next(); // return 'L'
    iterator.next(); // return 'e'
    iterator.next(); // return 'e'
    iterator.next(); // return 't'
    iterator.next(); // return 'C'
    iterator.next(); // return 'o'
    iterator.next(); // return 'd'
    iterator.hasNext(); // return true
    iterator.next(); // return 'e'
    iterator.hasNext(); // return false
    iterator.next(); // return ' '
    '''
    def __init__(self, compressedString):
        self.str = compressedString
        self.idx = 0
        self.cur = ' '
        self.cnt = 0

    def next(self):
        if not self.hasNext():
            return self.cur
        if self.cnt > 0:
            self.cnt -= 1
            return self.cur
        self.cur = self.str[self.idx]
        endIdx = self.idx+1
        while endIdx < len(self.str) and self.str[endIdx].isdigit():
            endIdx += 1

        self.cnt = int(self.str[self.idx+1:endIdx])
        self.cnt -= 1
        self.idx = endIdx
        return self.cur

    def hasNext(self):
        return self.cnt > 0 or self.idx < len(self.str)
iterator = StringIterator("L11e2t1C1o1d1e1")
print(iterator.next())
print(iterator.next())
print(iterator.next())
print(iterator.next())
print(iterator.next())
print(iterator.next())
print(iterator.next())
print(iterator.hasNext())
print(iterator.next())
print(iterator.hasNext())
print(iterator.next())