COS Pro 2급 대비 복습
주제: 리스트 처리와 조건문 기초
"""

# 패턴 1: 조건에 맞는 요소의 개수와 합계 구하기
def solution_count_and_sum(arr, K):
    """
    리스트 arr에서 K의 배수인 수들의 개수와 합을 반환
    (COS Pro 2급 단골: "특정 조건을 만족하는 수 찾기")
    """
    count = 0
    total = 0
    for x in arr:
        if x % K == 0:
            count += 1
            total += x
    return count, total

# 패턴 2: 최댓값과 최솟값을 제외한 평균 구하기
def solution_trimmed_mean(scores):
    """
    심사위원 점수 중 최고점과 최저점을 제외한 평균 산출
    (COS Pro 2급 단골: "데이터 가공 및 산술 연산")
    """
    if len(scores) <= 2:
        return 0
    
    total = sum(scores)
    max_score = max(scores)
    min_score = min(scores)
    
    # 전체 합에서 최고/최저 제외 후 개수(n-2)로 나누기
    result = (total - max_score - min_score) // (len(scores) - 2)
    return result

# 패턴 3: 문자열 교체 및 필터링
def solution_string_replace(s):
    """
    문자열에서 특정 문자를 바꾸거나 삭제하기 (예: 'a'를 'z'로)
    (COS Pro 2급 단골: "문자열 조작")
    """
    res = ""
    for char in s:
        if char == 'a':
            res += 'z'
        elif char == 'b':
            continue # 'b'는 삭제
        else:
            res += char
    return res

# --- 오늘 복습 결과 테스트 ---
if __name__ == "__main__":
    print("--- 패턴 1 테스트 (3의 배수) ---")
    c, s = solution_count_and_sum([3, 5, 9, 12, 15, 20], 3)
    print(f"개수: {c}, 합계: {s}") # 4개, 39

    print("\n--- 패턴 2 테스트 (최고/최저 제외 평균) ---")
    avg = solution_trimmed_mean([90, 80, 70, 60, 100])
    print(f"절삭 평균: {avg}") # (90+80+70)/3 = 80

    print("\n--- 패턴 3 테스트 (문자 조작) ---")
    print(f"결과: {solution_string_replace('abracadabra')}") # zrzczdzrz
