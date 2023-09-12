class DNode:
    def __init__(self, elem, prev=None, next=None):
        self.data = elem
        self.prev = prev
        self.next = next


# 이중연결덱
class doublyLinkedDeque:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front == None

    def clear(self):
        self.front = self.rear = None

    def size(self):
        node = self.front
        count = 0
        while not node == None:
            node = node.next
            count += 1
        return count

    # 전단삽입
    def addFront(self, item):
        node = DNode(item, None, self.front)
        if self.isEmpty():
            self.front = self.rear = node
        else:
            self.front.prev = node
            self.front = node

    # 후단삽입
    def addRear(self, item):
        node = DNode(item, self.rear, None)
        if self.isEmpty():
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    # 후단삭제
    def deleteFront(self):
        if self.isEmpty():
            pass
        else:
            data = self.front.data
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            else:
                self.front.prev = None
            return data

    # 전단삭제
    def deleteRear(self):
        if self.isEmpty():
            pass
        else:
            data = self.rear.data
            self.rear = self.rear.prev
            if self.rear == None:
                self.front = None
            else:
                self.rear.next = None
            return data

    def display(self, msg="DoublyLinkedDeque : "):
        print(msg, end="")
        node = self.front
        if self.isEmpty():
            print("None")
            return
        while not node == None:
            print(node.data, end=" ")
            node = node.next
        print()


# main
if __name__ == "__main__":
    DQ = doublyLinkedDeque()
    DQ.addFront(1)
    DQ.addFront(2)
    DQ.addRear(3)
    DQ.display()
    DQ.deleteRear()
    DQ.display()
    DQ.deleteFront()
    DQ.display()
    DQ.deleteFront()
    DQ.display()
