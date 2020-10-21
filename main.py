class DoubleNode:    
  def __init__(self, data, next=None, prev=None):
    self.data = data
    self.next = next
    self.prev = prev

#reverse
def solution(head_node):        
  current_node = head_node #print_nodes
    
  while current_node.next != None:        
    current_node = current_node.next
           
  tail_node = current_node   
   
  while current_node.prev != None: #reverse                    
    tmp = current_node.prev
    current_node.prev = current_node.next
    current_node.next = tmp
        
    if current_node.next == head_node:
      current_node.next.next = None
      current_node.prev = current_node
      break        
    current_node = current_node.next 
   
  return tail_node

def print_node(head):
  current_node = head #print_nodes
  print(current_node.data)
  while current_node.next != None:            
    current_node = current_node.next
    print(current_node.data)
    
               
items = [0, 1, 2, 3, 4, 5]
head_node = DoubleNode(items[0])
current_node = head_node
    
for item in items[1:]: #создание
  node = DoubleNode(item)
  current_node.next = node
  node.prev = current_node
  current_node = node

print_node(head_node)
print("##########REVERSE############")
head_node = solution(head_node)
print_node(head_node)
print("######################")