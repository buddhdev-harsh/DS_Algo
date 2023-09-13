class Insert:
  def __init__(self) -> None:
    pass

  def insertion_sort( self, arr):
    for i in range(1, len(arr)):
      element = arr[i]
      j = i-1

      while j >= 0 and element< arr[j]:
        arr[j+1] = arr[j]
        j -= 1

      arr[j+1] = element

    
arr = [9, 8, 7, 6 ,5, 4]

Is  = Insert()
Is.insertion_sort(arr)
print(arr)