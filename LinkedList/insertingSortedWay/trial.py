
class Node():
    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def getHead(self):
        return self.head

    def sortedInsert(self, new_node):
        if self.isEmpty():
            self.head = new_node
        # traverse node forward until finding smaller than v
        else:
            preNode = self.getHead()
            crtNode = self.getHead()
            crtValue = crtNode.value
            # loop until current value is smaller than new value
            while crtValue <= new_node.value:
                # previous node become current node
                preNode = crtNode
                # next of current node become current node
                crtNode = crtNode.next
                # current value become value of next node
                if crtNode != None:
                    crtValue = crtNode.value
                else:
                    break
            # new node is smaller than current node
            if new_node.value < preNode.value:
                new_node.next = preNode
                self.head = new_node
            else:
                preNode.next = new_node
                new_node.next = crtNode


        return self.getHead()

    def printList(self):
        crtNode = self.head
        while(crtNode.next != None):
            print(crtNode.value)
            crtNode = crtNode.next
        print(crtNode.value)


if __name__ == '__main__':
    # Driver program
    llist = LinkedList()
    new_node = Node(5)
    llist.sortedInsert(new_node)
    new_node = Node(10)
    llist.sortedInsert(new_node)
    new_node = Node(7)
    llist.sortedInsert(new_node)
    new_node = Node(3)
    llist.sortedInsert(new_node)
    new_node = Node(1)
    llist.sortedInsert(new_node)
    new_node = Node(9)
    llist.sortedInsert(new_node)
    print("Create Linked List")
    llist.printList()