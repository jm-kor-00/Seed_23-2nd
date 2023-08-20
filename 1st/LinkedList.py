from NodeModule import Node

#단순연결리스트
class linkedList:
    def __init__(self):
        self.head = None

    #공백여부 확인
    def isEmpty(self):
        return self.head == None
    
    #크기반환
    def size(self):
        node = self.head
        count = 0
        while not node == None:
            node = node.next
            count += 1
        return count
    
    #인덱스로 노드주소 찾기
    def getNode(self,pos):
        if pos < 0 : 
            return None
        node = self.head
        while pos > 0 and node != None:
            node = node.next
            pos -= 1
        return node
    
    #인덱스로 데이터 찾기
    def getEntry(self,pos):
        targetnode = self.getNode(pos)
        if targetnode == None : 
            return None
        else : 
            return targetnode.data

    #데이터 교체  
    def replace(self,pos,item):
        targetnode = self.getNode(pos)
        if targetnode != None :
            targetnode.data = item

    #데이터값으로 노드 찾기
    def find(self, data):
        node = self.head
        while node is not None:
            if node.data == data : return node
            node = node.next
        return None
    
    #pos번째에 새로운 데이터 삽입
    def insert(self,pos,elem):
        before = self.getNode(pos - 1)
        if before == None:
            self.head = Node(elem,self.head) 
        else :
            node = Node(elem,before.next)
            before.next = node

    #삭제
    def delete(self,pos):
        before = self.getNode(pos-1)
        if before == None :
            if self.head is not None :
                self.head = (self.head).next
        else :
            before.next = (before.next).next

    #출력
    def display(self,msg='LinkedStack : '):
        print(msg,end ='')
        node = self.head
        while not node == None:
            print(node.data,end =' -> ')
            node = node.next
        print(None)
    
    #리스트 초기화
    def clear( self ): 
        self.head = None

#main
if __name__ == "__main__":
    s = linkedList()
    for i in range(5):
        s.insert(i,i*10)
    s.insert(5,60)
    s.display()
    # s.insert(3,80)
    # s.display()

    print(s.getEntry(3))