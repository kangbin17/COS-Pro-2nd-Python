알고리즘 구현: DFS와 백트래킹을 이용한 순열 구하기
"""

def get_permutations(arr, r):
    """
    주어진 배열(arr)에서 r개의 요소를 뽑아 순서를 고려해 나열하는 모든 경우의 수를 구함.
    
    :param arr: 탐색할 원본 데이터 리스트
    :param r: 뽑을 요소의 개수
    :return: 생성된 순열 리스트가 담긴 2차원 배열
    """
    result = []
    visited = [False] * len(arr)
    
    def dfs(path):
        # 1. 종료 조건: 원하는 개수(r)만큼 요소를 다 뽑았을 때
        if len(path) == r:
            # path 배열은 계속 변형되므로 복사본을 결과에 저장
            result.append(path[:])
            return
            
        # 2. 탐색 로직: 배열을 처음부터 끝까지 확인
        for i in range(len(arr)):
            # 아직 방문하지 않은(뽑지 않은) 요소라면
            if not visited[i]:
                # 방문 처리 및 경로에 추가
                visited[i] = True
                path.append(arr[i])
                
                # 다음 깊이로 재귀 호출 (DFS)
                dfs(path)
                
                # 3. 백트래킹(상태 복구): 탐색을 마치고 돌아오면 이전 상태로 되돌림
                path.pop()
                visited[i] = False
                
    # 빈 경로에서 탐색 시작
    dfs([])
    return result

# --- 테스트 실행 ---
if __name__ == "__main__":
    elements = ['A', 'B', 'C']
    pick_count = 2
    
    permutations_result = get_permutations(elements, pick_count)
    
    print(f"배열 {elements}에서 {pick_count}개를 뽑는 순열:")
    for p in permutations_result:
        print(p)
    print(f"총 경우의 수: {len(permutations_result)}개")
