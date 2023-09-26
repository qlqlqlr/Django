import copy

N, M = map(int, input().split())

arr = [list(input()) for _ in range(M)]

cnt1 = 0
cnt2 = 0
result = 0

arr2 = copy.deepcopy(arr)
for i in range(M):
    for j in range(N - 1):
        if arr2[0][0] == 'W':
            if arr2[i][j] == 'W' and arr2[i][j+1] == 'W':
                arr2[i][j + 1] = 'B'
                cnt1 += 1
            
            elif arr2[i][j] == 'B' and arr2[i][j + 1] == 'B':
                arr2[i][j + 1] = 'W'
                cnt1 += 1

        else:
            if arr[i][j] == 'W' and arr[i][j+1] == 'W':
                arr[i][j + 1] = 'B'
                cnt2 += 1
            
            elif arr[i][j] == 'B' and arr[i][j + 1] == 'B':
                arr[i][j + 1] = 'W'
                cnt2 += 1    


for j in range(N):
    for i in range(M - 1):
        if arr2[i][j] == 'W':
            if arr2[i][j] == 'W' and arr2[i + 1][j] == 'W':
                arr2[i + 1][j] = 'B'
                cnt1 += 1

            elif arr2[i][j] == 'B' and arr2[i + 1][j] == 'B':
                arr2[i + 1][j] = 'W'
                cnt1 += 1
            
        else:
            if arr[i][j] == 'W' and arr[i + 1][j] == 'W':
                arr[i + 1][j] = 'B'
                cnt2 += 1

            elif arr[i][j] == 'B' and arr[i + 1][j] == 'B':
                arr[i + 1][j] = 'W'
                cnt2 += 1

    
if cnt1 > cnt2:
    print(cnt1)
else:
    print(cnt2)