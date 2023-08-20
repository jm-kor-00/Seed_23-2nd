from NodeModule import Node

#원형연결큐
class circularLinkedQueue:
    def __init__(self):
        self.tail = None

    #공백여부확인
    def isEmpty(self):
        return self.tail == None

    #개수 반환
    def size(self):
        if self.isEmpty():
            return 0
        count = 1
        node = (self.tail).link
        while not node == self.tail:
            node = node.link
            count += 1
        return count
    
    #삽입
    def enqueue(self,elem):
        node = Node(elem,None)
        if self.isEmpty():
            node.link = node #다음이 꼬리라서 자기 자신이니까
            self.tail = node #위와 같음
        else :
            node.link = (self.tail).link
            (self.tail).link = node
            self.tail = node
    
    #삭제
    def dequeue(self):
        if self.isEmpty() : 
            return None
        else :
            data = ((self.tail).link).data
            if (self.tail).link == self.tail :#하나밖에 없을 때
                self.tail = None
            else: #두개이상
                (self.tail).link = ((self.tail).link).link
            return data
    
    #전단참조
    def peek(self):
        if self.isEmpty() : pass
        else :
            return ((self.tail).link).data

    #출력
    def display(self,msg='CircularLinkedQueue : '):
        print(msg,end = '')
        if self.isEmpty():
            print(None)
            return
        node = (self.tail).link 
        while node != self.tail:
            print(node.data,end = ' ')
            node = node.link
        print(node.data)
    def clear( self ): self.tail = None

#main
if __name__ == "__main__":
    CLQ = circularLinkedQueue()
    
    for i in range(1,20):
        CLQ.enqueue(i)

    CLQ.dequeue()
    CLQ.dequeue()

    print(CLQ.peek())
    CLQ.display()