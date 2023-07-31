class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree_from_pre_in(preorder, inorder):
    if not preorder or not inorder:
        return None

    root_val = preorder[0]
    root = TreeNode(root_val)

    idx = inorder.index(root_val)

    root.left = build_tree_from_pre_in(preorder[1:1+idx], inorder[:idx])
    root.right = build_tree_from_pre_in(preorder[1+idx:], inorder[idx+1:])

    return root

def build_tree_from_post_in(postorder, inorder):
    if not postorder or not inorder:
        return None

    root_val = postorder[-1]
    root = TreeNode(root_val)

    idx = inorder.index(root_val)

    root.left = build_tree_from_post_in(postorder[:idx], inorder[:idx])
    root.right = build_tree_from_post_in(postorder[idx:-1], inorder[idx+1:])

    return root

def are_traversals_same_tree(preorder, inorder, postorder):
    # Build trees from the given traversals
    tree_pre_in = build_tree_from_pre_in(preorder, inorder)
    tree_post_in = build_tree_from_post_in(postorder, inorder)

    # Compare the resulting trees
    return are_trees_equal(tree_pre_in, tree_post_in)

def are_trees_equal(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False

    return (root1.val == root2.val and
            are_trees_equal(root1.left, root2.left) and
            are_trees_equal(root1.right, root2.right))

# Test the function with the given examples
inorder1 = [4, 2, 5, 1, 3]
preorder1 = [1, 2, 4, 5, 3]
postorder1 = [4, 5, 2, 3, 1]

inorder2 = [4, 2, 5, 1, 3]
preorder2 = [1, 5, 4, 2, 3]
postorder2 = [4, 1, 2, 3, 5]

print("Output:")
print("Example 1:", "Yes" if are_traversals_same_tree(preorder1, inorder1, postorder1) else "No")
print("Example 2:", "Yes" if are_traversals_same_tree(preorder2, inorder2, postorder2) else "No")

"""OUTPUT
Output:
Example 1: Yes
Example 2: No
"""