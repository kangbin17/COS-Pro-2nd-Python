#  팰린드롬(Palindrome) 판별기

## 문제 설명
주어진 단어(문자열)가 거꾸로 읽어도 본래의 단어와 동일한지(예: level, racecar, 토마토) 판별하는 알고리즘을 구현합니다.

##  문제 해결 전략 및 핵심 개념
단순히 반복문(`for` / `while`)을 사용하여 문자열의 양끝을 비교할 수도 있지만, 본 코드에서는 **파이썬의 내장 슬라이싱(Slicing) 기법**을 활용하여 가독성과 효율성을 극대화했습니다.

### 1. 파이썬 슬라이싱 `[start:stop:step]` 의 이해
- 파이썬의 리스트나 문자열은 `[시작:끝:간격]` 형태로 데이터를 자를 수 있습니다.
- 이 중 `step`(간격) 값을 `-1`로 설정하면, 문자열의 맨 끝에서부터 처음까지 역순으로 순회하며 새로운 문자열을 반환합니다.

### 2. 알고리즘 설계
1. `word[::-1]`을 통해 입력된 문자열을 통째로 뒤집어 `reversed_word`에 할당합니다.
2. `if word == reversed_word:` 구문을 통해 원본과 역순 본이 완벽히 일치하는지 확인합니다.
3. 일치하면 `True`, 다르면 `False`를 반환합니다.

##  Python 정답 코드
```python
def solution(word):
    # 파이썬 문자열 슬라이싱을 활용한 역순 문자열 생성
    # step을 -1로 지정하여 전체 문자열을 뒤집음 (Time Complexity: O(N))
    reversed_word = word[::-1]
    
    # 원본 단어와 뒤집힌 단어의 값(Value) 비교
    if word == reversed_word:
        return True
    else:
        return False

# Test Cases
print(f"'level' -> {solution('level')}")   # Expected: True
print(f"'python' -> {solution('python')}") # Expected: False
