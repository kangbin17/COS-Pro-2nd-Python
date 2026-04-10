# 1. 리스트에서 특정 값보다 큰 요소 개수 세기 (기초)
def count_over_threshold(arr, threshold):
    count = 0
    for x in arr:
        if x > threshold:
            count += 1
    return count

# 2. 최댓값과 최솟값의 차이 구하기 (내장 함수 활용)
def get_max_min_diff(arr):
    if not arr: return 0
    return max(arr) - min(arr)

# 3. 문자열 뒤집기 (역순 인덱싱 복습)
def reverse_string(s):
    # 방법 1: 슬라이싱 활용 (강력 추천)
    # s[::-1]은 처음부터 끝까지 -1 간격으로(뒤에서부터) 가져온다는 뜻
    return s[::-1]

# 4. 문자열 슬라이싱 실습 (어제 틀린 부분!)
def slicing_practice(s):
    # s[1:4]는 인덱스 1, 2, 3까지만 가져옴 (4는 포함 안 됨!)
    # 예: "apple" -> s[1:4]는 "ppl"
    return s[1:4]

# 5. 리스트 요소의 합계와 평균 (정수 나눗셈 주의)
def get_sum_and_avg(arr):
    total = sum(arr)
    avg = total // len(arr) # COS Pro에서는 보통 정수 몫(//)을 요구함
    return total, avg

# 6. 특정 문자 교체하기
def replace_char(s, target, replacement):
    res = ""
    for char in s:
        if char == target:
            res += replacement
        else:
            res += char
    return res
