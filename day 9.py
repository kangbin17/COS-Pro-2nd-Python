# 4. 등수 구하기 (순차 탐색)
# 정렬을 쓰지 않고, 나보다 점수 높은 사람을 만날 때마다 등수를 1씩 더하는 방식.
def calculate_ranks(score):
    answer = []
    for my_score in score:
        rank = 1
        for other_score in score:
            if other_score > my_score:
                rank += 1
        answer.append(rank)
    return answer


# 5. 교대 근무 배정 (모듈러 연산 활용)
# 인덱스가 n을 넘어가더라도 % n 처리를 통해 다시 0으로 순환되도록 짠 코드.
def max_working_time(time_table, n):
    work_times = [0] * n 
    
    for i, time in enumerate(time_table):
        worker_index = i % n
        work_times[worker_index] += time
        
    return max(work_times)


# 6. 사이즈별 수량 카운팅 (다중 조건문)
# elif를 사용해 이미 걸러진 조건(앞선 분기)을 중복해서 검사하지 않도록 효율화함.
def count_tshirt_sizes(people):
    answer = [0, 0, 0, 0] # S, M, L, XL
    
    for p in people:
        if p < 95:
            answer[0] += 1
        elif p < 100:
            answer[1] += 1
        elif p < 105:
            answer[2] += 1
        else:
            answer[3] += 1
            
    return answer


# 7. 카드 게임 (중복 제거 및 형변환)
# set() 함수 대신 in / not in 연산자를 써서 로직만으로 배열 내 중복을 제거함.
def play_card_game(cards):
    total_sum = 0
    unique_colors = []
    
    for card in cards:
        color = card[0]
        total_sum += int(card[1]) # 문자열을 정수로 형변환 필수
        
        if color not in unique_colors:
            unique_colors.append(color)
            
    color_count = len(unique_colors)
    
    if color_count == 1:
        return total_sum * 3
    elif color_count == 2:
        return total_sum * 2
    else:
        return total_sum * 1
