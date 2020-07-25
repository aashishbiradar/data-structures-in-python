# Node Class
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None
    
# Doubly Linked list Class
class DLinkedList:
    def __init__(self, arr):
        self.head = ref = Node(arr[0])
        for i in range(1,len(arr)):
            prev = ref
            ref.next = Node(arr[i])
            ref = ref.next
            ref.prev = prev
        self.tail = ref
        

# Code execution starts here 
if __name__=='__main__': 
    print('<== START ==>')
    arr = [1,2,3,4,5]
    print('Data Array', arr)

    print('inserting into/creating a linked list from data array')
    llist = DLinkedList(arr)

    # forward traversing linked list
    print('forward traversing linked list')
    head = llist.head
    while head:
        print(head.data)
        head = head.next
    
    # backward traversing linked list
    print('backward traversing linked list')
    tail = llist.tail
    while tail:
        print(tail.data)
        tail = tail.prev

    print('<== END ==>')