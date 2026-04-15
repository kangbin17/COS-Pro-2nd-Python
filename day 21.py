최소 거스름돈 동전 개수 구하기
def solution(money):
    answer = 0
    # 1. 가장 큰 동전부터 순서대로 배열을 만듦 (이게 '최소 개수'의 핵심!)
    coins = [500, 100, 50, 10]
    
    # 2. 동전을 하나씩 꺼내면서 확인
    for coin in coins:
        # 3. 현재 동전으로 줄 수 있는 최대 개수(몫)를 answer에 더함
        answer += money // coin 
        
        # 4. 동전을 주고 남은 나머지 돈으로 money를 업데이트
        money %= coin 
        
    return answer

# 테스트 케이스
print(solution(2760)) # 결과: 9
print(solution(830))  # 결과: 6

