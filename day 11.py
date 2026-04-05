from collections import deque

def find_shortest_path(maze, start, end):
    """
    2차원 미로에서 시작점부터 도착점까지의 최단 거리를 BFS로 탐색하는 함수.
    이동 가능한 길은 0, 벽은 1로 가정함.
    
    :param maze: 2차원 리스트 (0: 길, 1: 벽)
    :param start: 시작 좌표 튜플 (row, col)
    :param end: 도착 좌표 튜플 (row, col)
    :return: 최단 이동 칸 수 (도달 불가 시 -1 반환)
    """
    rows = len(maze)
    cols = len(maze[0])
    
    # 상하좌우 이동 벡터
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # BFS를 위한 큐 생성 및 초기화 (x, y, 이동 거리)
    queue = deque([(start[0], start[1], 1)])
    
    # 방문 처리를 위한 2차원 리스트 (False로 초기화)
    visited = [[False] * cols for _ in range(rows)]
    visited[start[0]][start[1]] = True
    
    while queue:
        x, y, dist = queue.popleft()
        
        # 목적지에 도착한 경우 현재까지의 거리 반환
        if (x, y) == end:
            return dist
            
        # 상하좌우 4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 미로 범위를 벗어나지 않는지 확인
            if 0 <= nx < rows and 0 <= ny < cols:
                # 이동할 수 있는 길(0)이고, 아직 방문하지 않은 곳이라면
                if maze[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))
                    
    # 큐가 빌 때까지 목적지를 찾지 못하면 도달 불가
    return -1

# --- 단위 테스트 (Unit Test) ---
if __name__ == "__main__":
    # 5x5 미로 (0: 길, 1: 벽)
    sample_maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    
    start_pos = (0, 0) # 좌측 상단
    end_pos = (4, 4)   # 우측 하단
    
    result = find_shortest_path(sample_maze, start_pos, end_pos)
    
    print("=== BFS 미로 탐색 결과 ===")
    if result != -1:
        print(f"최단 경로 발견: 총 {result}칸 이동")
    else:
        print("목적지에 도달할 수 없는 미로입니다.")
