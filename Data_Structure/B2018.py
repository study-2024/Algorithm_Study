# 연속된 자연수의 합 구하기
n = int(input())
count = 1
start_index = 1
end_index = 1
sum = 1

while end_index != n:
    if sum == n:
        count += 1
        end_index += 1 # end_index를 오른쪽으로 한 칸 이동
        sum += end_index # 연속된 자연수 범위를 한 칸 더 확장
    elif sum > n:
        sum -= start_index # 배열의 왼쪽 값 삭제
        start_index += 1 # start_index를 오른쪽으로 한 칸 이동
    else:
        end_index += 1
        sum += end_index

print(count)