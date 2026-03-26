from collections import deque

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def preOrderTraversal(node):
  if node is None:
    return
  print(node.data, end=", ")
  preOrderTraversal(node.left)
  preOrderTraversal(node.right)

def inOrderTraversal(node):
  if node is None:
    return
  inOrderTraversal(node.left)
  print(node.data, end=", ")
  inOrderTraversal(node.right)

def postOrderTraversal(node):
  if node is None:
    return
  postOrderTraversal(node.left)
  postOrderTraversal(node.right)
  print(node.data, end=", ")

def bfs_traversal(root):
    if root is None:
        return

    # Use a deque for efficient queue operations (popleft() is O(1))
    queue = deque([root])
    result = []

    while queue:
        # Dequeue a node from the front of the queue
        node = queue.popleft()
        result.append(node.value) # Process the node

        # Enqueue left child if it exists
        if node.left:
            queue.append(node.left)

        # Enqueue right child if it exists
        if node.right:
            queue.append(node.right)
    
    return result
