N = int(input())
A = [0]*N # 리스트 내 요소 개수를 N개로 만듦과 동시에 각 요소를 0으로 초기화

for i in range(N):
    A[i] = int(input())

stack = [] # 자연수를 넣을 스택 초기화
num = 1 # 스택에 넣을 자연수
result = True
answer = ""

for i in range(N):
    su = A[i] # 현재 수열 값 선언
    if su >= num: # 현재 수열 값 >= 오름차순 자연수: 값이 같아질 때까지 append() 수행
        while su >= num:
            stack.append(num)
            num += 1
            answer += "+\n"
        stack.pop()
        answer += "-\n"
    else:
        n = stack.pop()
        if n > su:
            print("No")
            result = False
            break
        else:
            answer += "-\n"

if result:
    print(answer)