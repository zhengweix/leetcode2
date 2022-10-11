class UnionFind(object):
    '''UnionFind Python class.'''

    def __init__(self, n):
        assert n > 0, "n must be strictly positive"
        self.n = n
        # every node is it's own parent in the beginning
        self.parent = [i for i in range(n)]

    def find(self, i):
        '''Find the parent of an element (e.g. the group it belongs to) and compress paths along the way.'''
        if self.parent[i] != i:
            # path compression on the way to finding the final parent
            # (i.e. the element with a self loop)
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def is_connected(self, x, y):
        '''Check whether X and Y are connected, i.e. they have the same parent.'''
        return True if self.find(x) == self.find(y) else False

    def union(self, x, y):
        '''Unite the two elements by uniting their parents.'''
        xparent, yparent = self.find(x), self.find(y)
        if xparent != yparent:
            # if these elements are not yet in the same set,
            # we will set the y parent to the x parent
            self.parent[yparent] = xparent

    @property
    def disjoint_set_count(self):
        '''Count the amount of disjoint sets.'''
        # For every node, add the parent to the list of all parents.
        # This represents all disjoint sets.
        unique_parents = set([self.find(i) for i in range(self.n)])
        # return the count
        return len(unique_parents)