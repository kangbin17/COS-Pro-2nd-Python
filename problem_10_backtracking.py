# COS Pro 2급 10번: 최단 경로 (백트래킹)
# 2026-03-25 복습 기록 - 강빈

min_value = 10000
rooms = []
visited = []
length = 0

def patrol(now, e_sum):
    global min_value
    
    # 1. 가지치기: 이미 신기록보다 많이 썼으면 포기!
    if e_sum >= min_value:
        return

    # 2. 모든 방 방문 완료 확인
    if 0 not in visited:
        # 마지막 방에서 다시 시작점(0)으로 돌아가는 비용 추가
        min_value = min(min_value, e_sum + rooms[now][0])
        return

    # 3. 다음 갈 수 있는 방 탐색
    for next_room in range(length):
        if next_room != now and visited[next_room] == 0:
            visited[next_room] = 1 # 방문 도장 꽝!
            patrol(next_room, e_sum + rooms[now][next_room]) # 다음 방으로
            visited[next_room] = 0 # 돌아오면서 도장 지우기 (백트래킹 핵심!)

def solution(arr, N):
    global length, rooms, visited, min_value
    visited = [0] * N
    visited[0] = 1 # 시작점 방문 표시
    length = N
    rooms = arr
    min_value = 10000
    patrol(0, 0)
    return min_value
