# This python file has traversal functions to perform traversal on Binary Tree


# function to perform inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)


# function to perform preorder traversal
def preorder(root):
    if root:
        print(root.value, end=" ")
        inorder(root.left)
        inorder(root.right)


# function to perform postorder traversal
def postorder(root):
    if root:
        inorder(root.left)
        inorder(root.right)
        print(root.value, end=" ")
