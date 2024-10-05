people = [70, 50, 80, 50]
limit = 100
num = len(people)
answer = 0

people.sort()

start = 0
end = num-1

while start < end:

    if people[start] + people[end] > limit:
        end -= 1
    elif people[start] + people[end] <= limit:
        start += 1
        end -= 1
        num -= 2
        answer += 1

answer += num

print(answer)

