#단순연결노드
class Node:
    def __init__(self, elem, link = None):
        self.data = elem
        self.next = link

#이중연결노드
class doublyLinkedNode:
    def __init__(self,elem,prev=None,next=None):
        self.data = elem
        self.prev = prev
        self.next = next