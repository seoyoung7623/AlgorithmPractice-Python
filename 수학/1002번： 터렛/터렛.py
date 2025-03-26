#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1002                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: seoyoung7623 <boj.kr/u/seoyoung7623>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1002                           #+#        #+#      #+#     #
#    Solved: 2025/03/24 09:15:13 by seoyoung7623  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
'''
1. 그리드 방식
2. 점과점사이의 거리
3. BFS

✅ 4. 수학적 접근
좌표에서 거리만큼의 원을 그린다.
두원의 교점이 적의 위치!!

이렇게 나누는 문제라고 생각을 못함.. 수학적 접근도 고려하자
# 중심이 같은 경우 d = 0

'''
T = int(input())
for test_case in range(T):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    cnt = 0
    d = ((x1-x2)**2+(y1-y2)**2)**0.5

    # 중심이 같은 경우
    if d == 0 and r1 == r2:
        cnt = -1
    elif d == 0 and r1 != r2:
        cnt = 0
    elif d == abs(r1-r2): # 내접
        cnt = 1
    elif d == r1+r2: # 외접
        cnt = 1
    elif abs(r1-r2) > d: # 원안에 원
        cnt = 0
    elif r1+r2 < d: # 원이 만나지 않음
        cnt = 0
    else:
        cnt = 2
    print(cnt)
            
