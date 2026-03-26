from utils.linked_list import Node, traverseAndPrint


def reverseList(head: Node) -> Node:
    prev, curr = None, head
    while curr != None:
      tmp = curr.next
      curr.next = prev
      prev, curr = curr, tmp
    return prev

def reverseListRecursive(head: Node) -> Node:
    while not head:
      return None
   
    newHead = head
    if head.next:
      newHead = reverseListRecursive(head.next)
      head.next.next = head
    head.next = None

    return newHead
   

# node1 = None
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(12)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

traverseAndPrint(node1)
reversedHead = reverseListRecursive(node1)
traverseAndPrint(reversedHead)