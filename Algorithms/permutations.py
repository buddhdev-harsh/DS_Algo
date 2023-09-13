
class Permute:
  res = set()
  def __init__(self) -> None:
    pass

  def permute(self, string, i):
    if i == len(string):
      self.res.add("".join(string))
      return 
    
    for j in range(i, len(string)):
      lst = [char for char in string]
      lst[i], lst[j] = lst[j], lst[i]
      self.permute(lst, i+1)

  def numPermute(self, string, number):
    if number == len(string):
      print(string)
      return

    for i in range(0, len(string)-number+1):
      substring = string[i:i+number]
      self.numPermute(substring, number)


# permute("ab", 0)
# print(res)
# print(6-3+1)
# print the all the substring of length number in a string 
permute = Permute()
permute.numPermute("hello,world!", 3)