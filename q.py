class Queue:
  def __init__(self) -> None:
    self.q = []

  def insertAtbeginning(self, val):
    self.q.insert(0, val)
    return True
  
  def insertAtEnd(self, val):
    self.q.append(val)
    return True
  
  def removeAtBeginning(self):
    del self.q[0]

  def removeAtEnd(self):
    del self.q[-1]

  def print(self):
    print(self.q)


mq = Queue()
mq.insertAtbeginning(5)
mq.insertAtbeginning(4)
mq.insertAtbeginning(3)
mq.insertAtEnd(6)
mq.insertAtEnd(7)
mq.print()


mq.removeAtBeginning()
mq.removeAtBeginning()
mq.removeAtEnd()
mq.print()