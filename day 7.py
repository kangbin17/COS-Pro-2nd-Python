 두 수의 합 (Two Sum) 최적화 알고리즘

 문제 설명
주어진 숫자 리스트(`nums`)에서 두 수를 더해 목표값(`target`)을 만들 수 있는 두 숫자의 인덱스를 찾아 반환합니다.
(단, 정답은 반드시 1개만 존재한다고 가정합니다.)

 문제 해결 전략 및 핵심 개념
초보자들은 보통 이중 `for`문을 돌려 모든 경우의 수를 더해봅니다. 하지만 이 방식은 데이터가 많아질수록 기하급수적으로 느려집니다. (시간 복잡도 O(N²))

이 코드는 파이썬의 딕셔너리(Dictionary)를 활용해 과거에 본 숫자를 기억해 두는 방식으로 속도를 혁신적으로 높였습니다.

알고리즘 설계 (해시맵 활용)
1. 빈 딕셔너리 `seen_numbers`를 만듭니다. (여기에 지나온 숫자와 인덱스를 기록할 예정)
2. 리스트를 처음부터 끝까지 딱 한 번만 순회합니다. (`for`문 1번)
3. 현재 숫자에서 목표값을 만들기 위해 '필요한 짝꿍 숫자(complement)'를 계산합니다. (`target - 현재 숫자`)
4. 만약 그 '짝꿍 숫자'가 이미 `seen_numbers`에 등록되어 있다면? 정답을 찾은 것이므로 바로 두 인덱스를 반환합니다!
5. 없다면, 현재 숫자와 인덱스를 `seen_numbers`에 등록하고 다음 숫자로 넘어갑니다.

 Python 정답 코드
```python
def solution(nums, target):
    # 지나온 숫자들의 값을 키(Key), 인덱스를 값(Value)으로 저장할 딕셔너리
    seen_numbers = {}
    
    # enumerate()를 쓰면 인덱스(i)와 값(num)을 동시에 꺼낼 수 있습니다!
    for i, num in enumerate(nums):
        complement = target - num  # 현재 숫자의 '짝꿍' 계산
        
        # 짝꿍이 이미 딕셔너리에 저장되어 있다면? 빙고!
        if complement in seen_numbers:
            return [seen_numbers[complement], i]
            
        # 짝꿍이 없다면 현재 숫자를 딕셔너리에 기록해 둠
        seen_numbers[num] = i
        
    return [] # 정답이 없는 경우 (문제 조건상 실행되지 않음)

# --- Test Cases ---
nums_list = [2, 7, 11, 15]
target_val = 9

print(f"리스트: {nums_list}, 목표 합: {target_val}")
print(f"정답 인덱스: {solution(nums_list, target_val)}") # Expected: [0, 1] (2 + 7 = 9)
