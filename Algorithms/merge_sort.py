class MergeSort:
  def __init__(self) -> None:
    pass

  def conquer(self, left, right, arr) -> None:
    i = j = k = 0
    len_a, len_b = len(left), len(right)

    while i < len_a and j < len_b:
      if left[i] <= right[j]:
        arr[k] = left[i]
        i += 1
      else:
        arr[k] = right[j]
        j += 1
      k += 1

    while i < len_a:
      arr[k] = left[i]
      i += 1
      k += 1
    while j < len_b:
      arr[k] = right[j]
      j += 1
      k += 1

  def divide(self, arr) -> None:
    if len(arr) <= 1:
      return 
      
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    self.divide(arr[:mid])
    self.divide(arr[mid:])

    self.conquer(left, right, arr)


data = [4, 5, 10, 1, 2, 3, 7]
mg   = MergeSort()
mg.divide(data)
print(data)