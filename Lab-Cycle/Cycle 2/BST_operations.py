# This python file has operation functions to perform insertion, deletion, Searching on a Binary search Tree


#function to perform insertion 
def insert(root, key, Node):
    if root is None:
        return Node(key)
    else:
        if root.value == key:
            return root
        elif root.value > key:
            root.left = insert(root.left, key, Node)
        else:
            root.right = insert(root.right, key, Node)
    return root


#function to perform searching
def search(root, key, Node):
    
    if root is None:
        return False
    
    #Checking that current node is key or not
    if  root.value == key:
        return True
    #If key is less than root.value then move to left node
    elif root.value > key:
        return search(root.left, key, Node)
    #If key is greater than root.value then move to right node
    else:
        return search(root.right, key, Node)
    

#function to perform deletion 
def delete(root, key, Node):
    
    def minValueNode(node):
        current = node

        while current.left is not None :
            current = current.left

        return current
    
    if root is None:
        return root
    
    if root.value > key:
        root.left = delete(root.left, key, Node)
    
    elif root.value < key:
        root.right = delete(root.right, key, Node)
    
    else :
        
        #if root has no left and right child
        if root.left is None and root.right is None :
            root = None

        #if root has no left child
        elif root.left is None :
            temp = root.right 
            root = None
            return temp
        
        #if root has no right child
        elif root.right is None :
            temp = root.left
            root = None
            return temp
        
        else :
            temp = minValueNode(root.right)

            root.value = temp.value
            root.right = delete(root.right, temp.value, Node)
    return root

    


