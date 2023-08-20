첫 편에서는 C#의 기본 구조와 'Hello World!' 프로그램을 통해 간략하게 C#을 소개하였습니다. 이번 편에서는 C#에서 어떻게 데이터를 저장하고 사용하는지, 그리고 데이터의 '타입'이 무엇인지에 대해 알아볼 것입니다.

### 변수란?

변수는 데이터를 저장하는 메모리의 공간입니다. 이 변수에 이름을 붙여서 특정 데이터에 접근하고 그 값을 변경할 수 있습니다.

예를 들어, 우리가 숫자 '5'를 저장하고 싶다면, 이 숫자를 저장할 변수를 만들고 그 변수에 '5'를 저장하게 됩니다.

### C#의 기본 데이터 타입

C#에서는 다양한 종류의 데이터를 다룰 수 있도록 여러 데이터 타입을 제공합니다. 일부 중요한 데이터 타입을 소개하겠습니다:

1. **int**: 정수를 저장합니다. 예: 1, 100, -33 등.
2. **double**: 소수점이 있는 숫자를 저장합니다. 예: 3.14, -0.001 등.
3. **char**: 단일 문자를 저장합니다. 예: 'A', '1', '가' 등.
4. **string**: 문자열을 저장합니다. 예: "Hello", "C# 초보자" 등.
5. **bool**: 참(`true`) 또는 거짓(`false`) 값만을 저장합니다.

### 변수 선언 및 초기화

변수를 사용하기 전에는 반드시 선언해야 합니다. 변수 선언은 데이터 타입과 변수 이름으로 이루어집니다.

```c#
int myNumber;
```

이렇게 선언된 변수에 값을 저장하려면 아래와 같이 합니다:

```c#
myNumber = 5;
```

또는, 선언과 동시에 값을 저장할 수도 있습니다:

```c#
int myNumber = 5;
```

### 예제: 여러 변수를 사용하여 간단한 프로그램 작성

```c#
using System;

namespace VariablesExample
{
    class Program
    {
        static void Main(string[] args)
        {
            int age = 25;
            double height = 175.5;
            char initial = 'J';
            string name = "John";
            bool isStudent = true;

            Console.WriteLine("Name: " + name);
            Console.WriteLine("Initial: " + initial);
            Console.WriteLine("Age: " + age);
            Console.WriteLine("Height: " + height + " cm");
            Console.WriteLine("Is a student? " + isStudent);
        }
    }
}
```

#### 해설

- 변수 `age`는 John의 나이를 저장하고, `height`는 그의 키를 저장합니다.
- `initial`과 `name`은 각각 John의 초기와 이름을 저장합니다.
- `isStudent`는 John이 학생인지 아닌지의 여부를 나타냅니다.

오늘은 변수와 C#의 기본 데이터 타입에 대해 배웠습니다. 다음 편에서는 이 변수들을 어떻게 활용하는지, 그리고 연산자에 대해 알아보겠습니다 😊