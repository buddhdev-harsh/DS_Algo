class Selection:
  def __init__(self) -> None:
    pass

  def selection_sort(self, arr):
    for ind in range(len(arr)):
      min_ind = ind
      for ind_j in range(ind, len(arr)):
        if arr[min_ind] > arr[ind_j]:
          min_ind = ind_j
      arr[min_ind], arr[ind] = arr[ind], arr[min_ind]

    
arr = [6, 5, 43,2, 1]
ss = Selection()
ss.selection_sort(arr)
print(arr)