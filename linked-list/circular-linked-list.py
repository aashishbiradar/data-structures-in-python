# Node Class
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
    
# Linked list Class
class CLinkedList:
    def __init__(self, arr):
        self.head = ref = Node(arr[0])
        for i in range(1,len(arr)):
            ref.next = Node(arr[i])
            ref = ref.next
        ref.next = self.head

# Code execution starts here 
if __name__=='__main__': 
    print('<== START ==>')
    arr = [1,2,3,4,5]
    print('Data Array', arr)

    print('inserting into/ creating a linked list from data array')
    llist = CLinkedList(arr)

    # traversing linked list
    print('traversing linked list')
    ref = head = llist.head
    print(ref.data)
    ref = ref.next
    while ref != head:
        print(ref.data)
        ref = ref.next

    print('<== END ==>')