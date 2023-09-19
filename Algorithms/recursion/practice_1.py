
def check_pali(s):
  left, right = 0, len(s)-1
  while left < right:
    if s[left] != s[right]:
      return False
    left += 1
    right -= 1
  return True

def print_all(s, k, st):
  if k == 0:
    print(s)
    return
  
  for ind in range(0, len(st)):
    s += st[ind]
    print_all(s, k-1, st)
    s = s[:-1]
  
# 3 : implement atoi recusrsively
def atoi(string, num):
  if string.isalpha():
    return 0
  if len(string) == 1:
    return int(string)+(num*10)
  
  num = int(string[0:1])+(num*10)

  return atoi(string[1:], num)



# st = "abcd"
# print_all("", 2, st)
# print(check_pali("999"))

# 3
# num = atoi("112", 0)
# print(num, type(num))


