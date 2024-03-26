#수 N개가 주어졌을 때 i번째 수에서 j번째 수까지의 합을 구하는 프로그램 작성
import sys
input=sys.stdin.readline
get, num=map(int,input().split())
array=map(int,input().split())
prefix_sum=[0]
temp=0

for i in array:
    temp=temp+i
    prefix_sum.append(temp) #누적 합을 계산하는 것 

for i in range(num):
    s, e=map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s-1]) #누적합: 마지막 - (마지막-1)