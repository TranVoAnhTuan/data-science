class Node:
    def __init__(self, data= None):
        self.data = data
        self.next = None
class ListNode:
    def __init__(self, val= None, next = None):
        self.val = val
        self.next = next
class LinkedList:
    #Function to initialize the Linked list object
    def __init__(self):
        self.head = None
    
    #Function to insert a new node at the beginning
    def insertHead(self, new_data):
        #1 & 2: Allocate the Node & put in data
        new_node = Node(new_data)
        # 3. Make next of new Node as head
        new_node.next= self.head
        # 4. Move the head to point to new Node
        self.head = new_node
     
     #Function to insert a new node after the given prev_node
    def insertAfter(self, prev_data, new_data):
        #1. check if the given prev_node exists
        if prev_data is Node:
            print('the given previous node must in LinkedList.')
            return
        #2. Create new node &
        #3. Put in the data
        new_node = Node(new_data)

        #4. if prev_data is at the first position
        if (prev_data == self.head.data):
            new_node.next = self.head.next
            self.head.next = new_node
            return
        #5. check if the node given prev_node exists
        head = self.head
        while(head.data != prev_data):
            head = head.next
            if head == None:
                return
        new_node.next = head.next
        head.next = new_node
    def append(self, new_data):
        #1. Create a new node
        #2. Put in the data
        #3. Set next as None
        new_node = Node(new_data)

        #4. if the Linked list is empty, then make the new node as head
        if self.head is None:
            self.head = new_node
            return
        
        #5. Else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next
        
        #6. Change the next of last node
        last.next = new_node
    
    #Function to append a new node at the end
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is Node:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node

    
    #Function to print LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end='->')
            temp = temp.next
    def search(self, li, key):
  
        # Base case
        if(not li):
            return False
  
        # If key is present in
        # current node, return true
        if(li.data == key):
            return True
  
        # Recur for remaining list
        return self.search(li.next, key)
    def reverseLLUsingStack(self, head):
 
        # Initialise the variables
        stack, temp = [], head
 
        while temp:
            stack.append(temp)
            temp = temp.next
 
        head = temp = stack.pop()
 
        # Until stack is not
        # empty
        while len(stack) > 0:
            temp.next = stack.pop()
            temp = temp.next
 
        temp.next = None
        return head
 


if __name__ == '__main__':
    ll = LinkedList()
    ll.insertHead(5)
    ll.append(3)
    ll.insertAfter(3,7)
    ll.printList()
    # print(ll)
    if ll.search(ll.head,3):
        print(True)
    else:
        print(False)
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print("Given linked list")
    temp = head
    while temp:
        print(temp.val, end=' ')
        temp = temp.next
    obj = LinkedList()
    print("\nReversed linked list")
    head = obj.reverseLLUsingStack(head)
    while head:
        print(head.val, end=' ')
        head = head.next
