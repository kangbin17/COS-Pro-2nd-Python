1. 주스 세트 분배 및 해체 로직 (자원 관리)
def solution(num_apple, num_carrot, k):
    answer = 0

    # 1. k와 무관하게 최대로 만들 수 있는 세트 수 계산
    if num_apple < (3 * num_carrot):
        answer = num_apple // 3
    else:
        answer = num_carrot

    # 2. 세트를 만들고 남은 잉여 자원 계산
    num_apple -= answer * 3
    num_carrot -= answer

    # 3. 버려야 할 과일(k)에서 잉여 자원 우선 차감
    i = 0
    k = k - (num_apple + num_carrot)

    # 4. 잉여 자원을 다 버리고도 k가 남았다면 완성된 세트 해체
    while k > 0:
        if i % 4 == 0:
            answer = answer - 1  # 완성된 세트를 부수므로 개수 감소(-)
        i = i + 1
        k = k - 1

    return answer

2. TV 프로그램 겹침 시간 계산 (타임라인 배열 활용)
def solution(programs):
    answer = 0
    used_tv = [0] * 25

    # 배열의 인덱스를 시간으로 활용하여 방송 시간에 +1씩 누적
    for program in programs:
        for i in range(program[0], program[1]):
            used_tv[i] = used_tv[i] + 1
            
    # 조건에 따라 누적된 시간 탐색
    for i in used_tv:
        if i >= 1:  # (주의) 만약 문제에서 '2대 이상 필요한 시간'을 요구했다면 i >= 2 로 변경!
            answer = answer + 1
            
    return answer

3. 배열 내 절반 값 존재 여부 탐색 (in 연산자)
def solution(arr):
    answer = 0
    
    # 배열의 요소를 하나씩 꺼내어 검사
    for i in arr:
        # i의 절반값(i / 2)이 arr 배열 안에 존재하는지 확인
        if i / 2 in arr:
            answer += 1
            
    return answer
