# 8-5. 최대 부분 증가수열

n = int(input())
nums = list(map(int, input().split()))
# 작은 부분; 최소한으로만들고 확장시키기
dy = [1] * n
# i가 증가수열의 가장 마지막일 때 -> 확장
for i in range(n):
    for j in range(i+1):
        if nums[i] > nums[j]:   # 더 작은 것이 있으면
            dy[i] = max(dy[j]+1, dy[i])   # 그 전의 가장 긴 길이와 비교

print(max(dy))


