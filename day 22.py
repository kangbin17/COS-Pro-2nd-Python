# 1. 2차원 배열 인덱스 방향 탐색 (가로, 세로, 대각선)
def board_sum(board, N):
    sum_x, sum_y, sum_d1, sum_d2 = 0, 0, 0, 0
    for i in range(N):
        for j in range(N):
            sum_x += board[i][j]  # 가로합 (행 고정, 열 이동)
            sum_y += board[j][i]  # 세로합 (열 고정, 행 이동)
            
    for i in range(N):
        sum_d1 += board[i][i]         # 주 대각선 (왼쪽 위 -> 오른쪽 아래)
        sum_d2 += board[i][N - 1 - i] # 반대 대각선 (오른쪽 위 -> 왼쪽 아래)


# 2. 색종이 겹치기 (조건문 및 대입/비교 연산자)

def paper_overlap(paper, color, from_r, to_r, from_c, to_c, GRAY):
    for r in range(from_r, to_r + 1):  # 끝값 포함을 위해 +1
        for c in range(from_c, to_c + 1):
            if paper[r][c] == 0:       # 빈 칸이면 색칠
                paper[r][c] = color
            elif paper[r][c] != color: # 빈 칸이 아니고, 다른 색이면 겹침 처리
                paper[r][c] = GRAY     

    # 정답 카운트 시 '='(대입)가 아닌 '=='(비교) 주의!
    # if C == paper[r][c]: answer += 1


# 3. 최빈값 구하기 (빈도수 배열 활용)

def find_mode(arr, N):
    frequency = [0] * 101  # 숫자 범위에 맞춘 바구니 생성
    for i in range(N):
        frequency[arr[i]] += 1  # 등장 횟수 누적
        
    max_freq, mode_num = 0, 0
    for i in range(101):
        if max_freq <= frequency[i]: # 빈도수가 같거나 더 크면 갱신
            max_freq = frequency[i]
            mode_num = i             # 그때의 인덱스가 가장 많이 나온 숫자
    return mode_num


# 4. 최대공약수(GCD)와 최소공배수(LCM) (유클리드 호제법)

def gcd(a, b):
    # 나머지가 0이 될 때까지 재귀 호출 (뒤의 놈을 앞으로, 나머지를 뒤로)
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    # 두 수의 곱을 최대공약수로 나눈 몫 (정수형 유지를 위해 // 사용)
    return (a * b) // gcd(a, b)


# 5. 원형 큐/뺑뺑이 로직 (나머지 연산자 활용)

def distribute_jelly(arr, N, J):
    idx = 0
    answer = 0
    while J > 0:
        want = arr[idx]
        J -= want
        answer = idx + 1         # 아이 번호는 인덱스 + 1
        idx = (idx + 1) % N      # 배열 끝에 도달하면 다시 0으로 순환
    return answer


# 6. 정해진 경로의 최소 비용 계산 (배열 인덱스 매핑)

def calculate_path_cost(arr, path):
    answer = 0
    for i in range(len(path) - 1):
        from_room = path[i]
        to_room = path[i+1]
        # 방 번호는 1부터, 인덱스는 0부터 시작하므로 반드시 -1 처리
        answer += arr[from_room - 1][to_room - 1] 
    return answer
