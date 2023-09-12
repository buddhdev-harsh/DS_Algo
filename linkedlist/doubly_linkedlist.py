
class Node:
  def __init__(self, val=None, next = None, prev = None) -> None:
    self.val = val
    self.next = next 
    self.prev = prev

class DoubleLinkedList:
  def __init__(self) -> None:
    self.head =None
    self.current = None

  def insert(self, val):
    node = Node(val, None, None)
    
    if self.head is None:
      self.head = node
      self.current = node
      return

    self.head.next, node.prev = node, self.head
    self.head = node

  def print(self):

    itr = self.current
    ss = ""
    while itr:
      ss += str(itr.val) + '->'
      itr = itr.next  
    ss += "Null"
    print(ss)
    


dbl = DoubleLinkedList()
dbl.insert(2)
dbl.insert(10)
dbl.insert(90)

dbl.print()


