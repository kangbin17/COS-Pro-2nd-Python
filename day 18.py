# 1. 사다리 타기 게임 (Swap과 인덱스 보정)
# 핵심: 사람의 숫자 체계(1번부터)를 컴퓨터의 인덱스(0번부터)로 맞추기 위해 -1을 해준다.

def solution_ladder(ladders, player):
    # ladders: [[1, 2], [3, 4], ...] (연결된 세로줄 번호)
    for e in ladders:
        # e[0]-1과 e[1]-1의 위치를 서로 맞바꿈 (Swap)
        temp = player[e[0]-1]
        player[e[0]-1] = player[e[1]-1]
        player[e[1]-1] = temp
        
    return player



# 2. 특정 기간의 기온 검사하기 (range 범위 설정)
# 핵심: "A번째 일과 B번째 일 사이"를 구할 때는 range(A + 1, B)를 사용한다.

def solution_temperature(temperature, A, B):
    answer = 0
    # A와 B 사이의 날짜들만 검사해야 하므로 인덱스 범위를 좁힘
    for i in range(A + 1, B):
        # 조건에 맞는 기온을 찾으면 answer 1 증가
        if temperature[i] > temperature[A] and temperature[i] > temperature[B]:
            answer += 1
            
    return answer



# 3. 종이 나눠주기 (조기 종료 return의 마법)
# 핵심: 데이터를 변경(K -= paper)하기 전에 미리 조건을 검사하고 즉시 탈출(return)한다.

def solution_paper(papers, K):
    # K: 보유한 전체 종이 수
    # i: 현재 인덱스(지금까지 종이를 완벽히 받은 사람 수와 동일)
    # paper: 현재 사람이 필요한 종이 수
    for i, paper in enumerate(papers):
        # 종이를 나눠주기 전에 남은 종이가 부족한지 '미리' 확인
        if K < paper:
            return i  # 부족하면 그 자리에서 즉시 함수 종료 후 i 반환
        
        K -= paper # 종이가 충분하면 나눠줌
        
    return len(papers) # 모든 사람이 종이를 다 받았을 경우 (문제 초기 설정값)
