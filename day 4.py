카드 게임 (리스트 슬라이싱과 함수 분리)
# [핵심] 리스트 슬라이싱 [start : stop : step] 활용
# start 인덱스부터 끝까지 2칸씩 점프하며 카드를 번갈아 뽑는 로직

def func_a(bundle, start):
    return bundle[start::2] # start부터 2칸씩 건너뛰기

# 메인 로직: A는 0번부터, B는 1번부터 카드를 가져감
a_cards = func_a(bundle, 0)[:n]
b_cards = func_a(bundle, 1)[:n]


조교 배정 (몫과 나머지 연산자 활용)
# [핵심] 산술 연산자를 현실 문제(그룹핑)에 대입하기
# 그룹을 꽉 채워 묶을 때는 '//' (몫), 남은 인원을 확인할 때는 '%' (나머지)

# m명씩 묶었을 때 기본적으로 필요한 조교의 수 (몫)
answer += students // m

# m명씩 묶고 남은 짜투리 학생이 있는지 확인 (나머지)
if students % m != 0:
    answer += 1  # 1명이라도 남았다면 조교 1명 추가 투입


최소 열량 구하기 (최솟값 초기화의 정석)
# [핵심] 최솟값을 찾기 위한 초기값은 항상 '가장 큰 수'로 설정해야 한다!
# 0으로 세팅하면 어떤 데이터를 넣어도 0보다 작아질 수 없는 치명적 버그 발생.

# 수정 전: min_cal = 0
# 수정 후: 파이썬의 무한대(Infinity) 기호 활용 -> 어떤 값이 들어와도 첫 값으로 갱신됨
min_cal = float('inf')

for cal in calories:
    if cal > min_cal:
        answer += (cal - min_cal) # 최솟값보다 많이 먹으면 운동
    else:
        min_cal = cal  # 새로운 최솟값 발견 시 갱신!
