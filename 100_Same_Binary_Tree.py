
from utils.binary_tree import Node, preOrderTraversal, inOrderTraversal, postOrderTraversal, bfs_traversal

def areSameTrees(tree1: Node, tree2: Node) -> bool:
    if not tree1 and not tree2:
        return True
    if not tree1 or not tree2:
        return False
    if tree1.value != tree2.value:
        return False
    
    
    isLeftSame = areSameTrees(tree1.left, tree2.left)
    isRightSame = areSameTrees(tree1.right, tree2.right)
    return isLeftSame and isRightSame

tree_root = Node(1, 
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