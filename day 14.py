"""
알고리즘 구현: 연속된 문자열 압축 (Run-Length Encoding)
작성일: 2026.04.08
"""

def compress_string(s):
    """
    연속해서 나타나는 문자의 개수를 세어 '문자+숫자' 형태로 압축함.
    예: 'aaabbcccc' -> 'a3b2c4'
    
    :param s: 압축할 원본 문자열
    :return: 압축된 문자열
    """
    # 1. 예외 처리: 빈 문자열이거나 길이가 1인 경우 그대로 반환
    if not s:
        return ""
    if len(s) == 1:
        return s + "1"
        
    compressed_chars = []
    count = 1
    
    # 2. 문자열 순회 (두 번째 문자부터 시작하여 이전 문자와 비교)
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            # 문자가 연속되면 카운트 증가
            count += 1
        else:
            # 다른 문자가 나오면 지금까지의 문자와 카운트를 리스트에 저장
            compressed_chars.append(s[i-1] + str(count))
            count = 1 # 카운트 초기화
            
    # 3. 루프가 끝난 후, 마지막으로 남아있는 문자와 카운트 처리
    compressed_chars.append(s[-1] + str(count))
    
    # 4. 리스트를 하나의 문자열로 결합하여 반환 (성능 최적화)
    return "".join(compressed_chars)

# --- 실전 테스트 ---
if __name__ == "__main__":
    test_cases = [
        "aaabbcccc",       # 일반적인 케이스
        "a",               # 단일 문자 (엣지 케이스)
        "abcdef",          # 압축이 전혀 안 되는 케이스
        "aabbbbcdddddee",  # 복합 케이스
        ""                 # 빈 문자열 (엣지 케이스)
    ]
    
    print("=== 문자열 압축 테스트 결과 ===")
    for idx, test_str in enumerate(test_cases, 1):
        result = compress_string(test_str)
        print(f"테스트 {idx}: '{test_str}' -> '{result}'")
