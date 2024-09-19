def check(ladder, N, H):
    for start in range(1, N+1):
        k = start
        for h in range(1, H+1):
            if ladder[h][k]:
                k += 1
            elif k > 1 and ladder[h][k-1]:
                k -= 1
        if start != k:
            return False
    return True

def solve(N, M, H, existing_lines):
    ladder = [[False] * (N+1) for _ in range(H+1)]
    for a, b in existing_lines:
        ladder[a][b] = True

    def backtrack(count, x, y):
        if count > 3:
            return float('inf')
        if check(ladder, N, H):
            return count
        ret = float('inf')
        for i in range(x, H+1):
            k = y if i == x else 1
            for j in range(k, N):
                if not ladder[i][j] and not ladder[i][j-1] and not ladder[i][j+1]:
                    ladder[i][j] = True
                    ret = min(ret, backtrack(count+1, i, j+2))
                    ladder[i][j] = False
            y = 1
        return ret

    ans = backtrack(0, 1, 1)
    return ans if ans < float('inf') else -1


N, M, H = map(int,input().split())
existing_lines = []

for _ in range(M):
    a,b = map(int,input().split())
    existing_lines.append((a,b))

print(solve(N, M, H, existing_lines))


