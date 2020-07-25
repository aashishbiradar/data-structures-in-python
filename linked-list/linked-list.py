# Node Class
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
    
# Linked list Class
class LinkedList:
    def __init__(self, arr):
        self.head = head = Node(arr[0])
        for i in range(1,len(arr)):
            head.next = Node(arr[i])
            head = head.next

# Code execution starts here 
if __name__=='__main__': 
    print('<== START ==>')
    arr = [5,1,3,2,4]
    print('Data Array', arr)

    print('creating a linked list from data array')
    llist = LinkedList(arr)

    # traversing linked list
    print('traversing linked list')
    head = llist.head
    while head:
        print(head.data)
        head = head.next

    print('<== END ==>')