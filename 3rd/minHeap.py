class MinHeap_tuple:
    def __init__(self):
        self.heap = []
        self.heap.append([None,None])

    #노드개수 반환
    def size(self): return len(self.heap) - 1
    #힙트리 공백 여부 반환
    def isEmpty(self) : return self.size() == 0
    #해당노드의 부모 노드 반환
    def Parent(self,i) : return self.heap[i//2]
    #해당노드의 왼쪽 자식 반환
    def Left(self,i) : return self.heap[i*2]
    #해당노드의 오른쪽 자식 반환
    def Right(self,i) : return self.heap[i*2 + 1]

    def display(self,msg = '최소힙트리 : ') :
        print(msg, self.heap[1:])

    def insert(self,prty,data) :
        self.heap.append([prty,data])
        i = self.size()
        while(i != 1 and prty < self.Parent(i)[0]):
            self.heap[i] = self.Parent(i)
            i = i // 2
        self.heap[i] = [prty,data]

    def delete(self):
        parent = 1
        child = 2
        if not self.isEmpty():
            hroot = self.heap[1] #현재 루트 노드 = 삭제대상
            last = self.heap[self.size()] #마지막 자식 노드
            while(child <= self.size()):
                #parent
                if child < self.size() and (self.Left(parent)[0] > self.Right(parent)[0]):
                    child += 1
                if last[0] <= self.heap[child][0]:
                    break
                self.heap[parent] = self.heap[child]
                parent = child
                child *= 2

            self.heap[parent] = last
            self.heap.pop(-1)
            return hroot
#main
if __name__ == "__main__":
    heap = MinHeap_tuple()
    dataSet = [[2,'a'],[3,'b'],[4,'c'],[8,'d'],[9,'e'],[3,'f'],[7,'g'],[3,'i'],[6,'j']]
    for elem in dataSet: heap.insert(elem[0],elem[1])

    heap.display('삽입 후 : ')
    heap.delete()      
    heap.display('삭제 후 : ')      
    heap.delete()
    heap.display('삭제 후 : ')      