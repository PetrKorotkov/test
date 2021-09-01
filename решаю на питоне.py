n = int(input())
a = list(map(int, input().split()))
ans = [0] * n
x = 1
p = 0
for i in range(n - 1):
	if a[i] > a[i + 1]:
		x += 1
	else:
		for j in range(p, i + 1):
			ans[j] = x
			p = i + 1
		x = 1
ans[-1] = 1
if i == n - 2 and x > 1:
	for j in range(p, n):
		ans[j] = x
print(*ans)
