from utils.binary_tree import Node

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

def isSubtree(tree1: Node, tree2: Node) -> bool:
    if not tree2:
        return True
    if not tree1:
        return False
    
    if areSameTrees(tree1, tree2):
        return True
    
    return (isSubtree(tree1.left, tree2) or isSubtree(tree1.right, tree2))
