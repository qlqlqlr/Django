# 듣보잡

N, M = map(int, input().split())

a = set()
b = set()

for i in range(N):
    a.add(input())

for j in range(M):
    b.add(input())

result = sorted(list(a & b))

print(len(result))

for i in result:
    print(i)