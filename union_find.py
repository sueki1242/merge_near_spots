# coding : utf-8

class UnionFind():
    """
    Implementation of Union-Find tree
    (with path compression and without rank).
    seealso:: https://www.slideshare.net/chokudai/union-find-49066733
    >>> from union_find import UnionFind
    >>> union_find = UnionFind(10)
    >>> union_find.belongsSameGroup(1,2)
    False
    >>> union_find.union(1,2)
    >>> union_find.belongsSameGroup(1,2)
    True
    >>> union_find.union(3,4)
    >>> union_find.union(4,5)
    >>> union_find.belongsSameGroup(3,5)
    True
    >>> union_find.belongsSameGroup(1,5)
    False
    >>> union_find.union(1,5)
    >>> union_find.belongsSameGroup(1,5)
    True
    >>> union_find.belongsSameGroup(2,3)
    True
    """
    def __init__(self, n):
        self.parent = [0] * n
        for i in range(0, n):
            self.parent[i] = i

    def __root(self, x):
        """calc group of node x"""
        if (x == self.parent[x]):
            return x
        self.parent[x] = self.__root(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """
        merge two groups.
        one is which node x belongs to,
        and another is which node y belongs to.
        """
        parent_x = self.__root(x)
        parent_y = self.__root(y)
        if (parent_x == parent_y):
            return
        self.parent[parent_x] = parent_y

    def belongsSameGroup(self, x, y):
        """
        returns True iff node x and y belong to the same group.
        """
        return (self.__root(x) == self.__root(y))