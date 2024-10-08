#1.
'''i = int
for i in range(1, 101):
    if i % 2 == 1:
        print(i)'''

#2.
'''for i in range(1, 51):
    if i % 3 == 0 | i % 5 ==0:
        print(i)'''

#3.
'''for i in range(1, 101):
    if i % 2 == 1 & i % 3 == 1:
        print(i)'''

#4.
'''x = input("첫 번째 숫자를 입력하시오:")
y = input("두 번째 숫자를 입력하시오")
x = int(x)
y = int(y)

for i in range(x, y+1):
    if i % 2 == 0:
        if i % 4 ==0:
            print(i)'''

#수정 코드
'''# 1. 1부터 100까지의 숫자 중 홀수만 출력합니다.
for i in range(1, 101):  # 1부터 100까지의 숫자를 순회합니다.
    if i % 2 == 1:  # i가 홀수인지 확인합니다.
        print(i)  # 홀수라면 출력합니다.

# 2. 1부터 50까지의 숫자 중 3의 배수이면서 5의 배수인 숫자를 출력합니다.
for i in range(1, 51):  # 1부터 50까지의 숫자를 순회합니다.
    if i % 3 == 0 and i % 5 == 0:  # i가 3의 배수이면서 5의 배수인지 확인합니다.
        print(i)  # 조건을 만족하면 출력합니다.

# 3. 1부터 100까지의 숫자 중 소수를 출력합니다.
for i in range(2, 101):  # 2부터 100까지의 숫자를 순회합니다.
    is_prime = True  # 소수 여부를 판단할 변수 초기화
    for j in range(2, int(i ** 0.5) + 1):  # 2부터 i의 제곱근까지의 숫자를 순회합니다.
        if i % j == 0:  # i가 j로 나누어 떨어지면 소수가 아닙니다.
            is_prime = False
            break  # 더 이상 확인할 필요가 없으므로 반복을 중단합니다.
    if is_prime:  # is_prime이 여전히 True라면 소수입니다.
        print(i)  # 소수를 출력합니다.

# 4. 사용자로부터 두 숫자를 입력받아 그 범위 내의 모든 숫자 중 짝수이면서 4의 배수인 숫자를 출력합니다.
x = input("첫 번째 숫자를 입력하시오: ")
y = input("두 번째 숫자를 입력하시오: ")
x = int(x)  # 첫 번째 숫자를 정수로 변환합니다.
y = int(y)  # 두 번째 숫자를 정수로 변환합니다.

for i in range(x, y + 1):  # 첫 번째 숫자부터 두 번째 숫자까지 순회합니다.
    if i % 2 == 0 and i % 4 == 0:  # i가 짝수이면서 4의 배수인지 확인합니다.
        print(i)  # 조건을 만족하면 출력합니다.
'''
