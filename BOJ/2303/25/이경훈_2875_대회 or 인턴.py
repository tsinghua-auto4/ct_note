N, M, K = map(int, input().split())

for i in range(K):
  if N // 2 >= M:
    N -= 1
  else:
    M -= 1

print(min(N // 2, M))




# n, m, k = map(int, input().split())

# while (k != 0):
#   if n > 2 * m:
#     n -= 1
#     k -= 1
#   else:
#     m -= 1
#     k -= 1

# cnt = 0
# while (n > 1 and m > 0):
#   n -= 2
#   m -= 1
#   cnt += 1
# print(cnt)