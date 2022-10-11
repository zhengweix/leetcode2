class Solution:
    '''
    Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
    A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

    Example 1:
    https://assets.leetcode.com/uploads/2021/04/28/subtree1-tree.jpg
    Input: root = [3,4,5,1,2], subRoot = [4,1,2]
    Output: true

    Example 2:
    https://assets.leetcode.com/uploads/2021/04/28/subtree2-tree.jpg
    Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
    Output: false

    Constraints:
    The number of nodes in the root tree is in the range [1, 2000].
    The number of nodes in the subRoot tree is in the range [1, 1000].
    -104 <= root.val <= 104
    -104 <= subRoot.val <= 104

    Tree, Depth-First Search, String Matching, Binary Tree, Hash Function

    Count Univalue Subtrees, Most Frequent Subtree Sum
    '''
    def isSubtree(self, root, subRoot):
        def helper(node1, node2):
            if not node1 or not node2:
                return node1 is node2
            return node1.val == node2.val and helper(node1.left, node2.left) and helper(node1.right, node2.right)

        queue = [root]
        while queue:
            node = queue.pop(0)
            if helper(node, subRoot):
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False

    def isSubtree1(self, root, subRoot):
        def helper(node1, node2):
            if not node1 or not node2:
                return node1 is node2
            return node1.val == node2.val and helper(node1.left, node2.left) and helper(node1.right, node2.right)

        def helper1(node):
            if not node:
                return node is subRoot
            if helper(node, subRoot):
                return True
            return helper1(node.left) or helper1(node.right)
        return helper1(root)

    def isSubtree2(self, root, subRoot):
        ans = False
        target = ''
        def helper(node):
            '''Return hash of sub-tree rooted at node.'''
            nonlocal ans
            if not node:
                return "$"
            left, right = helper(node.left), helper(node.right)
            sha = sha256()
            sha.update((left + str(node.val) + right).encode())
            if sha.hexdigest() == target:
                ans = True
            return sha.hexdigest()

        target = helper(subRoot)
        helper(root)
        return ans 