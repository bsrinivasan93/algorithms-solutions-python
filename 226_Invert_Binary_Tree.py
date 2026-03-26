from utils.binary_tree import Node, preOrderTraversal, inOrderTraversal, postOrderTraversal, bfs_traversal

def invertTree(root: Node) -> Node:
    if root is None:
        return
    
    tmp = root.left
    root.left = root.right
    root.right = tmp

    invertTree(root.left)
    invertTree(root.right)
    return root


# root = TreeNode('R')
# nodeA = TreeNode('A')
# nodeB = TreeNode('B')
# nodeC = TreeNode('C')
# nodeD = TreeNode('D')
# nodeE = TreeNode('E')
# nodeF = TreeNode('F')

# root.left = nodeA
# root.right = nodeB

# nodeA.left = nodeC
# nodeA.right = nodeD

# nodeB.left = nodeE
# nodeB.right = nodeF

# preOrderTraversal(root)
# print("\n")
# inOrderTraversal(root)
# print("\n")
# postOrderTraversal(root)
# print("\n")

tree_root = Node(4, 
                 Node(2, 
                      Node(1), 
                      Node(3)), 
                 Node(7, 
                      Node(6), 
                      Node(9)))

traversed_values = bfs_traversal(tree_root)
print("BFS Traversal Order:", traversed_values)
inverted_tree = invertTree(tree_root)
print("Inv BFS Traversal Order:", bfs_traversal(inverted_tree))