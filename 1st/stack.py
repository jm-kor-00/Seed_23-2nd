class Stack:
    def __init__(self,MAX):
        self.top = -1 #초기위치 -1,스택이 비었다는 뜻
        self.capacity = MAX #용량설정
        self.list = [None] * self.capacity #리스트 생성
    
    def size(self):
        return self.top + 1
    
    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top == self.capacity - 1
    
    def push(self,e):
        if self.isFull() :#꽉찬 스택에 push실행시
            return False
        else :
            self.top += 1
            self.list[self.top] = e

    def pop(self):
        if self.isEmpty() :
            return False
        else :
            self.top -= 1
            return self.list[self.top + 1]
        
    def peek(self):
        if self.isEmpty() :
            return False
        else :
            return self.list[self.top]
        
    def showStack(self):
        print(' 현재스택: ',end ='')
        for i in range(self.size()):
            print(self.list[i],end=',')
        print()

if __name__ == "__main__":
    stack = Stack(10)
    stack.showStack()

    for i in range(10):
        stack.push(i)

    stack.showStack()
    stack.pop()

    stack.showStack()