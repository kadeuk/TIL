# 사용자에게 문자열을 입력받고 그 문자열의 개수를 세서 딕셔너리 형태로 저장후 출력을 하는 문제

def count_letters(s):
    result = {}
    for char in s.lower(): # 입력받은 s를 모두 소문자로 변환해서 char로 넘겨준다
        if char.isalpha(): # 'isalpha'는 파이썬의 문자열ㅓ 메서드로 문자열이 알파벳 문자로만 이루어져 있는지를 검사한다.
            if char in result: # 만약 사용자가 a를 입력하고 그 a가 result라는 딕셔너리 안에 있다면
                result[char] += 1 # a를 result딕셔너리에 키 a의 값을 하나 증가 시키고
            else:
                result[char] = 1 # 없다면 a = 1 로 만들어라
    return result

# 사용자에게 입력받기
s = input("문자열을 입력하세요: ")

# 사용자에게 입력받은 문자로 함수를 실행시키기
letter_counts = count_letters(s)

print(letter_counts)