"""
🎯 2026-03-30 COS Pro 알고리즘 디버깅 및 코드 수정 리뷰
💡 핵심 목표: 눈에 보이는 예시 결과에 속지 않고, 숨겨진 예외 케이스까지 커버하는 논리적 코드 작성하기
"""

def review_01_temperature_range(temperature, A, B):
    """
    [문제 1] 기온 구하기 (A일과 B일 사이)
    - 핵심 교훈: 범위를 지정할 때 하드코딩(숫자 직접 입력)을 피하고, 
                 range()의 '미만' 속성을 정확히 활용할 것.
    """
    answer = 0
    # ❌ 버그 코드: for i in range(0, len(temperature)): (전체 기간을 검사함)
    # ❌ 하드 코딩: for i in range(1, B): (A가 1이 아닌 테스트 케이스에서 오답 발생)
    
    # ✅ 정답 코드: A 다음 날부터 B 전날까지만 정확히 검사
    for i in range(A + 1, B): 
        if temperature[i] > temperature[A] and temperature[i] > temperature[B]:
            answer += 1
    return answer


def review_02_paper_distribution(papers, K):
    """
    [문제 2] 종이 나눠주기
    - 핵심 교훈: 원하는 조건을 찾았을 때(종이가 부족해졌을 때) 
                 불필요한 추가 반복을 막기 위해 즉시 탈출(return/break)해야 함.
    """
    length = len(papers)
    for i, paper in enumerate(papers):
        K -= paper
        if K < 0:
            # ❌ 버그 코드: length = i (조건 만족 후에도 계속 덮어쓰기가 발생함)
            
            # ✅ 정답 코드 1: return i (즉시 함수 종료)
            # ✅ 정답 코드 2: break 사용
            length = i
            break 
    return length


def review_03_bottle_exchange(money, price, n):
    """
    [문제 3] 빈 병 교환하기
    - 핵심 교훈: 현실 세계의 논리(지불은 '-', 획득은 '+')를 정확히 매칭하고, 
                 변수(n)가 주어졌을 때 임의의 숫자로 하드코딩하지 말 것.
    """
    answer = money // price
    empty_bottle = money // price
    
    while n <= empty_bottle:
        # ❌ 버그 코드: empty_bottle = empty_bottle + n (마트에 병을 줬는데 내 병이 늘어나는 기적)
        # ❌ 하드 코딩: empty_bottle = empty_bottle - 1 (교환 기준이 바뀌면 오답)
        
        # ✅ 정답 코드: 교환 기준 개수(n)만큼 정확히 차감
        empty_bottle -= n 
        answer += 1
        empty_bottle += 1
    return answer


def review_04_desk_and_chair(chairs, desks, money):
    """
    [문제 4] 의자와 책상을 사고 싶어요
    - 핵심 교훈: 이중 for문을 이용한 완전 탐색(Brute Force). 
                 최댓값을 구하면서 예산 조건을 동시에 만족하는 복합 조건식 작성.
    """
    answer = 0
    for chair in chairs:
        for desk in desks:
            price = chair + desk
            # ✅ 정답 코드: 현재까지의 최댓값보다 크면서(비싸면서), 내 예산(money) 이하인가?
            if answer < price and price <= money:
                answer = price
    return answer


def review_05_function_composition(number):
    """
    [문제 5] 숫자 뒤집고 차이 구하기 (함수 조립)
    - 핵심 교훈: 함수가 요구하는 매개변수(Parameter)의 개수와, 
                 변수 이름(digit, convert_number)이 의미하는 바를 유추하여 알맞게 조립.
    """
    # func_b(number): 자릿수 구하기
    # func_c(number, digit): 숫자 뒤집기
    # func_a(num1, num2): 두 수의 차이 구하기
    
    # ✅ 정답 코드: 순서와 재료(인자)를 정확히 맞춤
    digit = func_b(number) 
    convert_number = func_c(number, digit) 
    answer = func_a(number, convert_number) 
    return answer


def review_06_matching_socks(socks):
    """
    [문제 6] 양말 짝 맞추기
    - 핵심 교훈: 파이썬의 리스트 컴프리헨션(빈 바구니 만들기) 이해.
                 쌍(Set)을 구할 때는 나머지(%)가 아닌 몫(//)을 사용하고, 값을 누적(+=)할 것.
    """
    answer = 0
    # 리스트 컴프리헨션: 0으로 채워진 크기 10의 배열 생성 (count = [0] * 10 과 동일)
    count = [0 for _ in range(10)] 
    
    for s in socks:
        count[s] += 1
        
    for c in count:
        # ❌ 버그 코드: answer = (c % 2) (값을 덮어쓰고, 나머지를 구함)
        # ✅ 정답 코드: 누적 연산자(+=)와 몫 연산자(//) 사용
        answer += (c // 2) 
    return answer


def review_07_defective_apples(weight, boxes):
    """
    [문제 7] 불량 사과 박스 찾기
    - 핵심 교훈: '정상'과 '불량'의 논리적 반대 관계(and -> or) 파악.
                 부동소수점 오차를 방지하기 위해 비율 계산 시 정수 연산(//) 활용.
    """
    answer = 0
    for x in boxes:
        # ❌ 버그 코드: if x < (weight * 11) // 10 and x > (weight * 9) // 10: (정상품을 찾음)
        
        # ✅ 정답 코드: 오차 범위 10%를 벗어나는 합집합(or) 조건
        # 컴퓨터의 소수점 오차를 막기 위해 * 0.9 대신 * 9 // 10 의 정수 연산을 사용한 것이 포인트!
        if x < (weight * 9) // 10 or x > (weight * 11) // 10:
            answer += 1
    return answer
