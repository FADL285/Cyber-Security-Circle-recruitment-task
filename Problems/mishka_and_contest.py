"""
*           Mohamed Fadl            *
! ==>>  Mishka and Contest Problem 
! ==>> Link: https://codeforces.com/contest/999/problem/A
"""

n, k = map(int, input().split())
l = list(map(int, input().split()))
max = 0

while l:
    if l[0] <= k:
        l.pop(0)
    elif l[-1] <= k:
        l.pop(-1)
    else:
        break
    max += 1
print(max)
