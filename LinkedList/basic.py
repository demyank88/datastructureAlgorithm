class node():
    def __init__(self):
        self.data = None
        self.next = None

    def displayNode(self):
        print(f'Data: {self.data}')

class linkedList():
    def __init__(self):
        self.first = None
        self.last = None

    def isEmpty(self):
        return self.first == None

    def insertFirst(self, data):
        newNode = node()
        newNode.data = data
        newNode.next = self.first
        self.first = newNode

    def insertLast(self, data):
        current = self.first
        while current.next != None:
            current = current.next

        newNode = node()
        newNode.data = data
        current.next = newNode

    def displayList(self):
        print("List all nodes")
        current = self.first
        while current.next != None:
            current.displayNode()
            current = current.next
        else:
            current.displayNode()

if __name__ == '__main__':
    mylist = linkedList()
    mylist.insertFirst(100)
    mylist.insertFirst(50)
    mylist.insertFirst(99)
    mylist.insertFirst(88)
    mylist.insertLast(9999999)

    mylist.displayList();