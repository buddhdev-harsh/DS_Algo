class Node:
  def __init__(self, val, next= None) -> None:
    self.val = val
    self.next = next


class LinkedList:
  def __init__(self, head= None) -> None:
    self.head = head
    self.current = None

  def insert(self, val) -> None:
    node = Node(val)
    if self.head is None:
      self.head = node
      self.current = node

    self.head.next = node
    self.head = node

  def size(self) -> int:
    count = 0

    itr = self.current
    while itr is not None:
      count += 1
      itr = itr.next

    return count
  
  def print(self)-> None:
    itr = self.current
    ss = ''
    while itr:
      ss += str(itr.val)+"->"
      itr = itr.next

    ss += "Null"
    print(ss)

  def delete(self, val):
    itr_prev = Node(None)

    while self.current:
      if self.current.val == val and self.current.next is not None:
        self.current = self.current.next
        itr_prev.next = self.current
        break
      
      if self.current.val == val and self.current.next is None:
        itr_prev.next = None
        break

      itr_prev = self.current
      self.current = self.current.next

  def insertAtEnd(self, val):
    itr =self.current
    while itr:
      itr = itr.next
    self.insert(val)


    def search(self, val) -> bool:
      itr = self.current

      while itr:
        if itr.val == val:
          return True
        itr = itr.next

      return False

  def inserAtBeginning(self, val):
    itr = self.current
    node = Node(val, itr)
    self.current = node

  def insertAfter(self, val, data):
    itr = self.current
    
    while itr:
      if itr.val == val:
        node = Node(data, itr.next)
        itr.next = node
      itr = itr.next
    return "not found"

# initialize linkedlist
lst = LinkedList()
lst.insert(1)
lst.insert(2)
lst.insert(4)
lst.print()

#size func
# size = lst.size()
# print(size)

# # search func basic
# print(lst.search(4))
# print(lst.search(900))

#delete func
# lst.delete(1)
# lst.print()

# insert at end
lst.insertAtEnd(25)
lst.print()

lst.inserAtBeginning(21)
lst.print()

lst.insertAtEnd(20)
lst.print()

lst.insertAfter(2, 100)
lst.print()

lst.insertAfter(4, 400)
lst.print()

lst.inserAtBeginning(90)
lst.print()