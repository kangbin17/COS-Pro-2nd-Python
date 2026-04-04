"""
알고리즘 스터디: 소수 찾기 최적화 (Sieve of Eratosthenes)
작성일: 2026.04.04
"""

def get_prime_numbers(n):
    """
    1부터 n까지의 숫자 중 소수를 찾아 리스트로 반환하는 함수
    시간 복잡도: O(N log log N)
    """
    if n < 2:
        return []

    # 1. 0부터 n까지의 리스트를 만들고, 처음에는 모두 소수(True)라고 가정
    is_prime = [True] * (n + 1)
    
    # 0과 1은 소수가 아니므로 False로 처리
    is_prime[0] = is_prime[1] = False

    # 2. 2부터 n의 제곱근까지만 검사하여 효율성 극대화
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # i가 소수라면, i의 배수들은 소수가 아니므로 모두 False 처리
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    # 3. 배열에서 True로 남아있는 숫자(인덱스)만 리스트 컴프리헨션으로 추출
    primes = [i for i, prime in enumerate(is_prime) if prime]
    
    return primes

# --- 테스트 실행 ---
if __name__ == "__main__":
    target_range = 50
    result = get_prime_numbers(target_range)
    print(f"1부터 {target_range}까지의 소수 개수: {len(result)}개")
    print(f"소수 목록: {result}")
