# https://leetcode.com/problems/merge-two-sorted-lists/description/
from utils.linked_list import Node, traverseAndPrint

def mergeTwoLists(list1: Node, list2: Node) -> Node:
    dummy = Node()
    tail = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
           tail.next = list2
           list2 = list2.next
        tail = tail.next
    
    if list1:
       tail.next = list1
    else:
       tail.next = list2

    return dummy.next

list1node1 = None
# list1node1 = Node(1)
# list1node2 = Node(2)
# list1node3 = Node(4)
# list1node1.next = list1node2
# list1node2.next = list1node3
# traverseAndPrint(list1node1)

# list2node1 = None
list2node1 = Node(1)
# list2node2 = Node(3)
# list2node3 = Node(4)
# list2node1.next = list2node2
# list2node2.next = list2node3
# traverseAndPrint(list2node1)

mergedSortedListHead = mergeTwoLists(list1node1, list2node1)
traverseAndPrint(mergedSortedListHead)

