1. 단어의 오타 수정하기 (이중 반복문)
def solution(words, word):
    count = 0
    for comp in words:
        for i in range(len(word)):
            if comp[i] != word[i]:
                count += 1
    return count

2. 커트라인 이상 인원수 세기 (카운팅)
def solution(scores, cutline):
    answer = 0
    for s in scores:
        if s >= cutline:
            answer += 1
    return answer
  3. 시험 등수 구하기 (인덱스 추적 및 append)
def solution(score):
    answer = []
    for i in range(len(score)):
        rank = 1
        for j in range(len(score)):
            if score[j] > score[i]:
                rank += 1
        answer.append(rank)
    return answer

4. 가장 오래 일한 사람 구하기 (나머지 연산자 %)
 def solution(score):
    answer = []
    for i in range(len(score)):
        rank = 1
        for j in range(len(score)):
            if score[j] > score[i]:
                rank += 1
        answer.append(rank)
    return answer
   
5. 신체 사이즈별 그룹 분류하기 (비교 연산자 체이닝)
def solution(people):
    answer = [0 for _ in range(4)]
    for i in people:
        if i < 95:
            answer[0] += 1
        elif 95 <= i < 100:
            answer[1] += 1
        elif 100 <= i < 105:
            answer[2] += 1
        elif i >= 105:
            answer[3] += 1
    return answer
  
6. 카드뽑기 게임 점수 계산 (2차원 리스트 형변환)
def solution(cards):
    answer = 0
    total_sum = 0
    
    for i in range(3):
        total_sum += int(cards[i][1])
        
    color1 = cards[0][0]
    color2 = cards[1][0]
    color3 = cards[2][0]
    
    if color1 == color2 and color2 == color3:
        answer = total_sum * 3
    elif color1 == color2 or color2 == color3 or color1 == color3:
        answer = total_sum * 2
    else:
        answer = total_sum
        
    return answer
