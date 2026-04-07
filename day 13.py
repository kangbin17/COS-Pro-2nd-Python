제목: feat: 다익스트라(Dijkstra) 알고리즘을 이용한 최적 경로 탐색 구현
import heapq

def dijkstra(graph, start):
    # 거리 저장소 (무한대로 초기화)
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    # 우선순위 큐 (거리, 노드)
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue
            
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, [distance, neighbor])
                
    return distances

# 운전면허 학원에서 집까지의 가상 경로 테스트
my_map = {
    'Driving_School': {'Point_A': 5, 'Point_B': 2},
    'Point_A': {'Home': 1},
    'Point_B': {'Point_A': 2, 'Home': 5},
    'Home': {}
}

print(f"최단 경로 계산 결과: {dijkstra(my_map, 'Driving_School')}")
