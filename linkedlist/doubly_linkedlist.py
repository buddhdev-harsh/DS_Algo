
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

    print(self.head.prev.val)

    itr = self.head
    ss = ""
    while itr is not None:
      ss += str(itr.val) + '->'
      itr = itr.prev
    print(ss)
    
    # itr = self.head
    # ss = ''
    # while itr.prev:
    #   ss += str(itr.val) + '->'
    #   itr = itr.prev
    # ss += "Null"
    # print(ss)

dbl = DoubleLinkedList()

dbl.insert(2)
dbl.insert(10)
dbl.insert(90)

dbl.print()


