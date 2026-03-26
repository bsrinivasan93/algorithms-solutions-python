# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def traverseAndPrint(head):
        currentNode = head
        while currentNode:
            print(currentNode.val, end=" -> ")
            currentNode = currentNode.next
        print("null")