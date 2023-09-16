#   @platform: Codeforces
#   @problem_code: 1851B
#   @author: Aashray Bavisa
#   @since: 15 SEP 2023
#   @link: https://codeforces.com/contest/1851/problem/B

t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    # print(n, arr)
    sArr = sorted(arr)
    movements = 1
    l = 0
    while movements > 0 and arr != sArr and l < len(arr):
        movements = 0
        for j in range(l, len(arr)):
            for k in range(j,len(arr)):
                if arr[j] % 2 == arr[k] % 2 and arr[k] < arr[j]:
                    arr[j], arr[k] = arr[k], arr[j]
                    movements += 1
        l += 1
    if (arr == sArr):
        print("YES")
    else:    
        print("NO")
