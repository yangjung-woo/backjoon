a = int(input())
cnt = 0
while a != 0:  # =0 까지
    if a % 2 == 1: # 2로 나눴을때 나머지가 1이면 자리에 이진법 자리 1 추가 0에서 부터
        cnt += 1
    a = a // 2 #
print(cnt)
# 이 문제는 숫자 X를 이진수로 표현했을때 ex) 01001100 3번 1이 몇번 나오는지 출력하는 간단 코드다 