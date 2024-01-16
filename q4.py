class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inOrderSuccessor(root, node):
    if node.right is not None:
        return minValueNode(node.right)
    succ = None
    while root is not None:
        if node.val < root.val:
            succ = root
            root = root.left
        elif node.val > root.val:
            root = root.right
        else:
            break
    return succ

def inOrderPredecessor(root, node):
    if node.left is not None:
        return maxValueNode(node.left)
    pred = None
    while root is not None:
        if node.val > root.val:
            pred = root
            root = root.right
        elif node.val < root.val:
            root = root.left
        else:
            break
    return pred

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def maxValueNode(node):
    current = node
    while current.right is not None:
        current = current.right
    return current
