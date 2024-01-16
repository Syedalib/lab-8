def minValue(root):
    current = root
    while current.left is not None:
        current = current.left
    return current.val

def maxValue(root):
    current = root
    while current.right is not None:
        current = current.right
    return current.val