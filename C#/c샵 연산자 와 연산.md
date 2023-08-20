### 들어가기 전에

안녕하세요! 지난 편에서는 변수와 C#의 주요 데이터 타입들에 대해 알아보았습니다. 오늘은 이 변수들과 함께 자주 사용되는 연산자들에 대해 살펴볼 것입니다.

### 연산자란?

연산자는 데이터(변수, 리터럴 등)에 대한 연산을 수행하는 기호 또는 단어입니다. 예를 들면 덧셈, 뺄셈, 비교 등의 연산을 나타내는 기호를 생각해볼 수 있습니다.

### 주요 연산자들

1. **산술 연산자**:
    
    - `+`: 덧셈
    - `-`: 뺄셈
    - `*`: 곱셈
    - `/`: 나눗셈
    - `%`: 나머지
2. **비교 연산자**:
    
    - `==`: 같음
    - `!=`: 다름
    - `<`: 작음
    - `>`: 큼
    - `<=`: 작거나 같음
    - `>=`: 크거나 같음
3. **논리 연산자**:
    
    - `&&`: AND
    - `||`: OR
    - `!`: NOT

### 예제: 연산자를 사용한 간단한 프로그램

```c#
using System;

namespace OperatorsExample
{
    class Program
    {
        static void Main(string[] args)
        {
            int a = 10;
            int b = 3;
            
            Console.WriteLine("a + b = " + (a + b));
            Console.WriteLine("a - b = " + (a - b));
            Console.WriteLine("a * b = " + (a * b));
            Console.WriteLine("a / b = " + (a / b));
            Console.WriteLine("a % b = " + (a % b));
            
            Console.WriteLine("a == b? " + (a == b));
            Console.WriteLine("a > b? " + (a > b));
            
            bool isMorning = true;
            bool isRainy = false;
            Console.WriteLine("Is it a rainy morning? " + (isMorning && isRainy));
        }
    }
}
```

- 위의 프로그램에서 `a`와 `b`는 각각 10과 3의 값을 갖는 정수 타입의 변수입니다.
- 연산자를 사용해 여러 연산을 수행하고, 그 결과를 출력합니다.
- 마지막으로 `isMorning`과 `isRainy`는 불리언 타입의 변수로, 현재 날씨와 시간 상태를 나타냅니다.

오늘은 연산자와 그 연산들에 대해 배웠습니다. 다음 편에서는 조건문과 제어 구조에 대해 알아보도록 하겠습니다.😊