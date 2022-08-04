'''
https://leetcode.com/problems/binary-tree-level-order-traversal/
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Solution:
__________

Using Queue:
Push root node into the queue.
Till queue size is not 0, we can run the loop.
- Keep two lists, one level list(subset) and second that carries the list of level_lists
- Pop the items from the queue and keep them in the subset. This has to be done until the
number of nodes in the current level is echausted.
- Also, if there are further children, make sure to insert them into the queue for next iteration.
- Keep appending the subset into the resultant list and clear the subset.
- 
'''
import queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        res=[]
        q.append(root)
        while q:
            curlen = len(q)
            subset=[]
            for _ in range(curlen):
                temp = q.popleft()
                subset.append(temp.val)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            res.append(subset)
        return res
