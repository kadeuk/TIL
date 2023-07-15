# 사용자에게 숫자를 입력받아 입력받은 숫자의 팩토리얼을 계산하는 함수

def factorial():
    num = int(input('숫자를 입력하세요: '))
    result = 1 # 팩토리얼을 계산하기 위해서 result를 1로 둔다

    for i in range(1, num + 1): # range는 입력받은 숫자 전까지 i에 넣기 때문에 1을 더 해준다
        result *= i

    
    print(f'{num}의 팩토리얼은 {result}입니다.') # print문은 함수 안에 존재해야 한다

factorial()  # 함수를 실행