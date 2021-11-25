# import sys
# sys.stdin = open("input.txt", "rt")
cnt = 0
N = int(input())
NbyN = [[0]*N for in range(N)]
rowSum =[0]*N
columnSum = [0]*N
crossSum =0
for i in range(N):
    NbyN[i] = list(map(int,input().split()))
    rowSum[i] = sum(NbyN[i])
    for j in range(N):
        columnSum[j] += NbyN[i][j]
        if i==j or i+j == N-1:
            crossSum += NbyN[i][j]
