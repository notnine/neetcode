# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        print("preorder: " + str(preorder))
        print("inorder: " + str(inorder))

        if not preorder or not inorder:
            print("root: None")
            print()
            return None
        
        if len(preorder) == 1 or len(inorder) == 1:
            print("root: " + str(preorder[0]))
            print()
            return TreeNode(preorder[0])

        # preorder: self, left, right
        # inorder: left, self, right

        # get the root
        root = TreeNode(preorder[0])
        print("root: " + str(preorder[0]))
        print()

        # build left sub tree (recurse)
        # get index of self in inorder to determine partition
        self_index = inorder.index(root.val) # notice left subtree has self_index elements
        left = self.buildTree(preorder[1:self_index + 1], inorder[:self_index])

        # build right sub tree (recurse)
        right = self.buildTree(preorder[self_index + 1:], inorder[self_index + 1:])

        # attach left & right sub tree to root & return root
        root.left, root.right = left, right
        return root