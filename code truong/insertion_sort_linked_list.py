class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insertion_sort(head):
    if not head or not head.next:
        return head

    # Create a dummy node to serve as the head of the sorted linked list
    dummy = Node(0, head)

    # Traverse the linked list and insert each node into the sorted linked list
    curr = head
    while curr and curr.next:
        if curr.val <= curr.next.val:
            curr = curr.next
        else:
            prev = dummy
            while prev.next.val <= curr.next.val:
                prev = prev.next
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

    return dummy.next
