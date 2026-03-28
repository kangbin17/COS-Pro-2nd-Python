주스 만들기 (Logic: Loop & Resource Management)
# 핵심: 토끼 먹이(k)가 부족할 때, 만들어둔 주스를 취소(-)하여 재료를 확보함
# 주스 1잔 = 사과 3개 + 당근 1개 = 총 4개의 재료

while k > 0:
    if i % 4 == 0:
        answer = answer - 1  # [한 줄 수정] 주스를 해체해서 재료로 돌림
    i = i + 1
    k = k - 1


TV 애청자 (Logic: List Counting)
# 핵심: 리스트(used_tv)의 각 인덱스에 저장된 '켜진 TV 대수'를 확인
# '2대 이상' 켜진 시간만 카운트하는 것이 포인트

for i in used_tv:
    if i >= 2:  # [한 줄 수정] 1이 아니라 2 이상일 때만 answer 증가
        answer = answer + 1

  상담 학생 찾기 (New: Enumerate & Indexing)
# enumerate는 [인덱스, 값]을 동시에 반환함
# idx: 컴퓨터 순서(0부터), i: 스케줄 내용('O', 'X')

for idx, i in enumerate(schedule):
    if i == "X":  # [빈칸] 선생님이 없는 날("X") 확인
        answer.append(idx + 1)  # [빈칸] 0번 학생은 없으므로 idx에 1을 더함


# 리스트 슬라이싱 기본 구조: [start : stop : step]

arr = [0, 1, 2, 3, 4, 5]

print(arr[::2])    # [0, 2, 4] -> 0번부터 끝까지 2칸씩 점프
print(arr[1::2])   # [1, 3, 5] -> 1번부터 끝까지 2칸씩 점프 (홀수 인덱스)
print(arr[::-1])   # [5, 4, 3, 2, 1, 0] -> 리스트 뒤집기
