#  이진 탐색 (Binary Search) 알고리즘

##  문제 설명
오름차순으로 정렬된 숫자 리스트(`arr`)가 주어질 때, 우리가 찾고자 하는 목표값(`target`)이 리스트의 몇 번째 인덱스에 있는지 찾아서 반환합니다. 만약 리스트에 값이 없다면 `-1`을 반환합니다.

##  문제 해결 전략 및 핵심 개념
리스트의 처음부터 끝까지 하나씩 찾는 '순차 탐색(Linear Search)'은 데이터가 많아질수록 속도가 급격히 느려집니다. (시간 복잡도 O(N))
이를 해결하기 위해 **'업다운 게임'의 원리**를 코드로 구현했습니다.

### 알고리즘 설계
1. 탐색할 범위의 맨 왼쪽 끝을 `left`, 맨 오른쪽 끝을 `right`로 설정합니다.
2. 두 지점의 중간 위치인 `mid`를 계산하여, 그곳의 값과 `target`을 비교합니다.
3. **업(Up)!** `target`이 중간값보다 크면? ➔ 정답은 무조건 오른쪽에 있으므로 탐색 범위를 오른쪽 절반으로 좁힙니다. (`left = mid + 1`)
4. **다운(Down)!** `target`이 중간값보다 작으면? ➔ 정답은 무조건 왼쪽에 있으므로 탐색 범위를 왼쪽 절반으로 좁힙니다. (`right = mid - 1`)
5. 값을 찾을 때까지 이 과정을 반복합니다.

##  Python 정답 코드
```python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    # left가 right보다 커지면 탐색할 공간이 없다는 뜻 (종료 조건)
    while left <= right:
        mid = (left + right) // 2  # 중간 인덱스 계산 (소수점은 버림)
        
        if arr[mid] == target:
            return mid  # 정답을 찾은 경우 인덱스 반환
            
        elif arr[mid] < target:
            # 타겟이 더 크면, 오른쪽 절반만 탐색
            left = mid + 1
            
        else:
            # 타겟이 더 작으면, 왼쪽 절반만 탐색
            right = mid - 1
            
    return -1  # 리스트 안에 타겟이 없는 경우

# --- Test Cases ---
# 반드시 '정렬된' 리스트를 사용해야 합니다.
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target_val = 13

print(f"리스트: {numbers}")
print(f"찾는 숫자 {target_val}의 인덱스는? : {binary_search(numbers, target_val)}") # Expected: 6
