# 점수조작. 자기점수중 최대값을 고른다. 최대값이 M일때 모든 점수를 점수/M *100으로 고쳤다.
#세준이의 성적을 이 방법으로 계산했을 때 새로운 평균을 구하는 프로그램을 작성하시오 

n=input()
mylist=list(map(int, input().split()))
#map 함수 = 반복하는 함수
#split 함수 = 숫자를 구분짓는 함수
#위에서 map 함수를 쓰지 않을 경우 input받은 숫자를 하나하나 split해서 하나한 int 형식으로 변환해줘야함! 
mymax=max(mylist)
sum=0

for i in mylist:
    sum=sum+int(i)

print(sum/mymax*100/int(n))