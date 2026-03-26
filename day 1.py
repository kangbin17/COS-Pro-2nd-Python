01_shirt_size.py (1번: 함수 구현)
def solution(shirt_size):
    answer = [0, 0, 0, 0, 0, 0] # 6개 사이즈 바구니 준비
    for s in shirt_size:
        if s == "XS":
            answer[0] += 1
        elif s == "S":
            answer[1] += 1
        elif s == "M":
            answer[2] += 1
        elif s == "L":
            answer[3] += 1
        elif s == "XL":
            answer[4] += 1
        elif s == "XXL":
            answer[5] += 1
    return answer




02_discount.py (2번: 함수 구현)
def solution(price, grade):
    answer = 0
    if grade == "S":
        answer = price * 0.95
    elif grade == "G":
        answer = price * 0.90
    elif grade == "V":
        answer = price * 0.85
    return int(answer) # 정수로 변환 필수!




08_palindrome.py (8번: 한 줄 수정)
def solution(sentence):
    str = ''
    for c in sentence:
        if c != '.' and c != ' ': # or를 and로 고쳤던 부분!
            str += c
    size = len(str)
    for i in range(size // 2):
        if str[i] != str[size - 1 - i]:
            return False
    return True
