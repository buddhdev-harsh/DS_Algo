from typing import Union

class Binary_search:
  def __init__(self, lst, ele) ->  None:
    self.ele = ele
    self.lst = lst
    self.ans = self.search(self.ele)

  def search(self, ele) -> Union[int, bool]:
    left, right = 0, len(self.lst)-1

    while left <= right:
      
      mid = (left+right) //2
      if self.lst[mid] == self.ele:
        return mid
      elif ele < self.lst[mid]:
        right = mid-1
      else:
        left = mid+1

    return False

  def recursive(self,left, right)-> Union[int, bool]:
    
    if left > right:
      return False
    
    mid = (left+right)//2
    
    if self.lst[mid] == self.ele:
      return mid
    elif self.ele < self.lst[mid]:
      return self.recursive( left, mid-1)
    else:
      return self.recursive( mid+1, right)

arr = [5, 6, 19, 41, 56, 77]
bs  = Binary_search(arr, 5)

# print("Found at index:"+ str(bs.ans) if bs.ans is not False else "not found")
ind = bs.recursive( 0, len(arr)-1)
print("found at index:"+str(ind) if ind is not False else "Not Found")