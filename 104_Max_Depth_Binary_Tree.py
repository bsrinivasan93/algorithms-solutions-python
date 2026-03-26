
from utils.binary_tree import Node, preOrderTraversal, inOrderTraversal, postOrderTraversal, bfs_traversal

def maxDepth(root: Node) -> int:
    if root is None:
        return 0
    
    leftDepth = maxDepth(root.left)
    rightDepth = maxDepth(root.right)
    return max(leftDepth, rightDepth) + 1

tree_root = Node(3, 
                 Node(9, 
                      None, 
                      None), 
                 Node(20, 
                      Node(15), 
                      Node(7)))

tree_root_2 = Node(1,
                   None,
                   Node(2))

print("BFS Traversal Order:", bfs_traversal(tree_root_2))
print(maxDepth(tree_root_2))