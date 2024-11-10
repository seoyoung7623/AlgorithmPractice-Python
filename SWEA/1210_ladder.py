# 1210 Ladder
# 구현문제
# 알고리즘 접근은 맞으나 SWEA에 테스트케이스가 10개 존재하는데 그중 N번째를 실행하는 문제임..
# 문제 출력을 실수

T = 10
# 10개의 테스트케이스가 존재한다는게 뭐야..
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    n = 100
    # 사다리 아래서부터 올라간것
    # 왼쪽 오른쪽에 1이 있는경우가 위 아래보다 우선순위가 높다
    # 위, 오, 왼 / 벽 확인해야됨 [-1,0],[0,1],[0,-1]
    # 만약 오른쪽으로 갔는데 왼쪽으로 갈수도 있는가? 있다. 그래서 오론쪽이면 계속 오른쪽으로 가야됨
    # 위로 올라다가 왼/오 를 만나면 이동하다가 위를 만남 이게 한 반복
    # 종료조건: x행이 0인경우의 y값 
    ladder = [list(map(int,input().split())) for _ in range(n)] 
    
    y = ladder[n-1].index(2)
    x = n-1
    while x != 0:
        # 오른쪽이 1이면 오른쪽으로 이동, 0 나올 때까지 계속 + 위로 한 칸
        if 0 <= y + 1 <= 99 and ladder[x][y + 1] == 1:
            while y + 1 <= 99 and ladder[x][y + 1] == 1:
                y += 1
            x -= 1
        # 왼쪽이 1이면 왼쪽으로 이동, 0 나올 때까지 계속 + 위로 한 칸
        elif 0 <= y - 1 <= 99 and ladder[x][y - 1] == 1:
            while 0 <= y - 1 and ladder[x][y - 1] == 1:
                y -= 1
            x -= 1
        # 좌우에 1이 없으면 위로 한 칸 이동
        else:
            x -= 1
        
    print(f'#{N} {y}')
   