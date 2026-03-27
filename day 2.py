# [2차 1번] 리스트 인덱스로 개수 세기
def count_gloves(gloves):
    counter = [0 for _ in range(max(gloves) + 1)]
    for x in gloves:
        counter[x] += 1 # 인덱스 x를 바구니 주소로 사용!
    return counter

# [2차 5번] while문과 break 활용
def attack_monster(attack, recovery, hp):
    count = 0
    while(True):
        count += 1
        hp -= attack
        if hp <= 0: # 0이 되는 순간 즉시 탈출!
            break
        hp += recovery
    return count

# [2차 6번] range(1, length)로 이전 값과 비교하기
def elevator_dist(floors):
    dist = 0
    for i in range(1, len(floors)): # 1번부터 시작해야 i-1(이전 층)이 존재함
        diff = floors[i] - floors[i-1]
        dist += abs(diff) # 절댓값으로 이동 거리 합산
    return dist
