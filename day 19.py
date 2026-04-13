1. [리스트 순회] 이전 날짜와 비교하기
def solution(temperatures):
    answer = 0
    # 인덱스 1부터 시작하는 이유: 0번째 날은 '이전 날'이 없기 때문!
    for i in range(1, len(temperatures)):
        # 오늘 기온(i)이 어제 기온(i-1)보다 높다면 카운트 증가
        if temperatures[i] > temperatures[i-1]:
            answer += 1
            
    return answer

# [테스트 코드] 깃허브에 같이 올려두고 실행해봐!
temps = [25, 27, 26, 29, 30, 28]
print("결과:", solution(temps)) # 예상 출력: 3


2. [조건부 연산] 등급별 할인율 적용하기
def solution(price, grade):
    answer = 0
    
    # 등급에 따른 할인율 적용 (S: 5%, G: 10%, V: 15%)
    # 실수(float)로 계산되므로 반드시 int()로 감싸서 정수로 만들어야 함!
    if grade == "S":
        answer = int(price * 0.95)
    elif grade == "G":
        answer = int(price * 0.90)
    elif grade == "V":
        answer = int(price * 0.85)
        
    return answer

# [테스트 코드]
print("S등급 10000원:", solution(10000, "S")) # 예상 출력: 9500
print("V등급 50000원:", solution(50000, "V")) # 예상 출력: 42500


3. [최대/최소 제외] 체조 경기 점수 계산하기
def solution(scores):
    answer = 0
    
    # 1단계: 리스트에서 가장 큰 값과 작은 값 찾기
    max_score = max(scores)
    min_score = min(scores)
    
    # 2단계: 전체 합에서 최고점, 최저점 빼기
    total = sum(scores) - max_score - min_score
    
    # 3단계: 남은 점수들의 개수로 나누어 평균 구하기
    # 2개를 뺐으므로 전체 길이에서 2를 빼줌. // 연산자로 정수 몫만 취함.
    answer = total // (len(scores) - 2)
    
    return answer

# [테스트 코드]
score_list = [35, 28, 98, 34, 20, 50, 85, 74, 71, 7]
print("평균 점수:", solution(score_list)) # 예상 출력: 47
