class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class LL():
    def __init__(self):
        self._head = None
    def insertLL(self,e):
        new_node = Node(e)
        if self._head is None:
            self._head = new_node
        else:
            n = self._head
            while n:
                if n.next is not None:
                    n = n.next
                else:
                    n.next = new_node 
                    n = new_node.next
            
    def display(self):
        a = self._head
        while a:
            print(a.val)
            a = a.next

    def merge_sort(self, head):
        if not head or not head.next:
            return head
        
        # Step 1: Divide the linked list into two halves
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head1, head2 = head, slow.next
        slow.next = None
        
        # Step 2: Recursively sort each half of the linked list
        head1 = self.merge_sort(head1)
        head2 = self.merge_sort(head2)
        
        # Step 3: Merge the two sorted halves by creating a new sorted list
        dummy = Node(0)
        tail = dummy
        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next
        if head1:
            tail.next = head1
        if head2:
            tail.next = head2
        
        return dummy.next
    

test = LL()
test.insertLL(1)
test.insertLL(2)
test.insertLL(5)
test.insertLL(4)
test.insertLL(3)
test.insertLL(6)
test.display()
sorted_list = test.merge_sort(test._head)
print("Sorted linked list:")
while sorted_list:
    print(sorted_list.val)
    sorted_list = sorted_list.next