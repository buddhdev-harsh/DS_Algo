class Sorting:
  def __init__(self) -> None:
    pass

  def bubble_sort(self, arr)-> list:
    for i in range(len(arr)):
      for j in range(i, len(arr)-1):
        if arr[i] > arr[j]:
          arr[i], arr[j] = arr[j], arr[i]

    return arr

  def selection_sort(self, arr):
    for ind in range(len(arr)):
      min_ind = ind
      for ind_j in range(ind, len(arr)):
        if arr[min_ind] > arr[ind_j]:
          min_ind = ind_j
      arr[min_ind], arr[ind] = arr[ind], arr[min_ind]

  def merger(self, left, right, arr):
    i, j, k = 0, 0, 0
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
      
  def merge(self, arr):
    if len(arr) <= 1:
      return

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    self.merge(left)
    self.merge(right)

    self.merger(left, right, arr)

  def insertion_sort( self, arr):
    for i in range(1, len(arr)):
      element = arr[i]
      j = i-1

      while j >= 0 and element< arr[j]:
        arr[j+1] = arr[j]
        j -= 1

      arr[j+1] = element
  
  def swap(self, a, b, arr):
    if a != b:
      temp = arr[a]
      arr[a] = arr[b]
      arr[b] = temp

  def quicksort(self,arr, start, end):
    if start < end:
      pi = self.partition(arr, start, end)
      self.quicksort(arr, start, pi-1)
      self.quicksort(arr, pi+1, end)

  def partition(self, arr, start, end):
    pivot_index = start
    
    while start < end:
      while start < len(arr) and arr[start] < arr[pivot_index]:
        start += 1
      while end >= 0 and arr[end] > arr[pivot_index]:
        end -= 1

      if start < end:
        self.swap(start, end, arr)
    
    self.quicksort(arr, pivot_index, end)
    
    return end


    

arr = [5, 2, 1, 8, 9]
sort = Sorting()
sort.merge(arr)
print(arr)