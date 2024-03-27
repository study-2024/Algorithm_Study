# 숫자의 합 구하기
N = int(input())

sum = 0
numbers = list(input())
for i in numbers:
    sum += int(i)

print(sum)