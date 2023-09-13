class Sorting:
  def __init__(self) -> None:
    pass

  def bubble_sort(self, arr)-> list:
    for i in range(len(arr)):
      for j in range(i, len(arr)-1):
        if arr[i] > arr[j]:
          arr[i], arr[j] = arr[j], arr[i]

    return arr
  

arr = [5, 2, 1, 8, 9]
sort = Sorting()
arr = sort.bubble_sort(arr)
print(arr)