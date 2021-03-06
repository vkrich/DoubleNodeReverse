class MyQueue(list):  
  def __init__(self, items = []):
    self.items = items
  def pop(self):
    try:
      first_elem = self.items[0]
      self.items = self.items[1:]  
      print(first_elem)    
      return first_elem 
    except IndexError:
      return None  
    
  def push(self, x):
    self.items.append(x)

  def size(self):
    print(len(self.items))
    return len(self.items)

  def peek(self):
    try:
      print(self.items[0])
      return self.items[0]
    except IndexError:
      return None  

qu = MyQueue()

print("############Queue#############")
for _ in range(int(input())):
  command = input().split()
  try:
    eval(f'qu.{command[0].strip()}({command[1].strip()})')
  except IndexError:
    eval(f'qu.{command[0].strip()}()')

print("##############DoubleNode################")

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
    
def del_item(head, k):  
  if k<=0: #nedative cases
    print("Wrong k, no element found")
    return head

  k-=1
  current_node = head

  if k==0:
    head = current_node.next     
    return head 
  try:
    for _ in range(k-1):      
      current_node = current_node.next   
    current_node.next = current_node.next.next
  except AttributeError:
    print("Wrong k, no element found")    
  return head

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
head_node = del_item(head_node, 7)
print_node(head_node)