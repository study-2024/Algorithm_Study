n = 4
A =[[0] * (n+1)]

for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)
    print(A)