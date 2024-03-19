n = input()                              # n에 과목의 수 입력
mylist = list(map(int, input().split())) # mylist에 점수 정보 저장
mymax = max(mylist)                      # mymax에 mylist 정보 중 최댓값 저장
sum = sum(mylist)                        # sum에 mylist 모든 데이터 값 더하기

print(sum * 100 / mymax / int(n))