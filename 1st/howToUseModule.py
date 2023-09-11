from collections import deque

####################################

#스택으로 사용
STACK = deque()

#append
STACK.append(1)
STACK.append(2)

#pop 
말단삭제 = STACK.pop()

####################################

#큐로 사용
Queue = deque()

#enqueue
Queue.append(1)
Queue.append(2)

#dequeue
전단삭제 = Queue.popleft()

####################################

#덱으로 사용

Deque = deque()

#전단삽입
Deque.appendleft(1)

#전단삭제
전단삭제 = Deque.popleft()

#말단삽입
Deque.append(2)

#말단삭제
말단삭제 = Deque.pop()