a = 15


count = 1
start = 1
end = 1
sum_v = 1

while start <= a // 2:

    if sum_v < a:
        end += 1
        sum_v += end
    elif sum_v > a:
        sum_v -= start
        start += 1
    elif sum_v == a:
        count += 1
        sum_v -= start
        start += 1

print(count)