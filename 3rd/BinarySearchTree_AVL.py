class BSTNode:				            
    def __init__ (self, key, value):	
        self.key = key		        	
        self.value = value	          	
        self.left = None		    	
        self.right = None

#순환으로 구현한 탐색 메소드
def search_bst(n, key) :		
    if n == None :
        return None
    elif key == n.key:		        	
        return n
    elif key < n.key:			        
        return search_bst(n.left, key)	
    else:				                
        return search_bst(n.right, key)
    
#반복으로 구현한 탐색 메소드
def search_bst_iter(n, key) :
    while n != None :			        
        if key == n.key:		        
            return n
        elif key < n.key:		        
            n = n.left			        
        else:				            
            n = n.right			        
    return None
			        
#value가 일치하는 노드 반환 메소드
def search_value_bst(n, value) :
    if n == None : return None
    elif value == n.value:					
        return n
    res = search_value_bst(n.left, value) 	
    if res is not None :					
       return res							
    else :									
       return search_value_bst(n.right, value)
    
#반복으로 구현된 최대 키 노드 반환 메소드
def search_max_bst(n) :	
    while n != None and n.right != None:
        n = n.right
    return n

#반복으로 구현된 최소 키 노드 반환 메소드
def search_min_bst(n) :	
    while n != None and n.left != None:
        n = n.left
    return n

#순환으로 구현된 삽입 연산
def insert_bst(r, n) :
    if n.key < r.key:			
        if r.left is None :		
           r.left = n			
           return True
        else :			    	
           return insert_bst(r.left, n)	
    elif n.key > r.key :	        	
        if r.right is None :	    	
           r.right = n		        	
           return True
        else :			            	
           return insert_bst(r.right, n)
    else : 				        
        return False	
    		
#자식이 없을 때 삭제 메소드
def delete_bst_case1 (parent, node, root) :
    if parent is None: 			    
        root = None			        
    else :
        if parent.left == node : 	
            parent.left = None		
        else :				        
            parent.right = None		
    return root			    
        
#자식이 하나일 때 삭제 메소드
def delete_bst_case2 (parent, node, root) :
    if node.left is not None :	
        child = node.left		
    else :						
        child = node.right		

    if node == root :			
        root = child			
    else :
        if node is parent.left : 	
            parent.left = child		
        else :			        	
            parent.right = child	

    return root	

#자식이 둘일 때 삭제 메소드
def delete_bst_case3 (node, root) :
    succp = node		        	
    succ = node.right		    	
    while (succ.left != None) :		
        succp = succ			
        succ = succ.left

    if (succp.left == succ) :		
        succp.left = succ.right		
    else :			            	
        succp.right = succ.right	

    node.key = succ.key	    		
    node.value= succ.value	    	
    node = succ;	

    return root	

#삭제연산
def delete_bst (root, key) :
    if root == None : return None       		
    parent = None                       		
    node = root                         	    
    while node != None and node.key != key :	
        parent = node
        if key < node.key : node = node.left
        else : node = node.right

    if node == None : return None

    if node.left == None and node.right == None: #자식이 없을 때
        root = delete_bst_case1 (parent, node, root)

    elif node.left==None or node.right==None : #자식이 하나일 때
        root = delete_bst_case2 (parent, node, root)
        
    else : #자식이 둘일 때
        root = delete_bst_case3 (node, root)

if __name__ == "__main__":
    A = BSTNode('A',1)
    B = BSTNode('B',2)
    C = BSTNode('C',3)
    D = BSTNode('D',4)
    E = BSTNode('E',5)
    F = BSTNode('F',6)