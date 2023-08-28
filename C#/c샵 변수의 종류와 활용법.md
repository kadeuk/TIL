C# 언어에서 변수는 데이터를 저장하고 액세스하는 데 사용되는 중요한 요소입니다. 이 게시물에서는 C#에서 제공하는 다양한 변수 유형, 그것들의 개념, 사용법 및 활용법에 대해 자세히 알아보겠습니다.

#### **1. 변수란?**

변수는 메모리에 저장된 데이터 값에 대한 참조 또는 이름입니다. 이를 통해 프로그래머는 데이터에 접근하고, 수정하고, 조작할 수 있습니다.

#### **2. C#에서의 변수 종류**

C#에서는 다양한 데이터 유형을 위한 여러 변수 유형을 제공합니다:

- **기본 데이터 유형**: `int`, `float`, `double`, `char`, `bool` 등
- **참조 데이터 유형**: `string`, 객체, 배열 등

#### **3. 변수 선언 및 초기화**

변수를 사용하기 전에 선언해야 합니다. 변수 선언은 다음과 같습니다:

```c#
int age;
```

변수를 선언하면서 동시에 초기화할 수도 있습니다:

```c#
int age = 25;
```

#### **4. 변수의 활용법**

##### **기본 데이터 유형의 활용:**

```c#
int score = 90;
double average = 85.5;
char grade = 'A';
bool isPassed = true;

Console.WriteLine($"Score: {score}, Average: {average}, Grade: {grade}, Passed: {isPassed}");
// 결과: Score: 90, Average: 85.5, Grade: A, Passed: True
```

##### **참조 데이터 유형의 활용:**

```c#
string name = "John Doe";
Console.WriteLine($"Hello, {name}!");  // 결과: Hello, John Doe!
```

#### **5. 변수의 활용 예제**

변수는 다양한 프로그래밍 문제를 해결하는 데 활용됩니다. 예를 들어, 사용자로부터 입력받은 두 숫자의 합을 계산하는 간단한 프로그램은 다음과 같습니다:

```c#
using System;

namespace SumApp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter first number:");
            int num1 = int.Parse(Console.ReadLine());

            Console.WriteLine("Enter second number:");
            int num2 = int.Parse(Console.ReadLine());

            int sum = num1 + num2;
            Console.WriteLine($"The sum of {num1} and {num2} is: {sum}");
        }
    }
}
```

- `using System;`
    
    - 기본적인 입출력 기능을 제공하는 System 네임스페이스를 포함시킵니다.
- `namespace SumApp`
    
    - 코드를 `SumApp`이라는 네임스페이스 안에 정의합니다. 이는 코드의 조직화와 관리를 도와줍니다.
- `class Program`
    
    - `Program`이라는 클래스를 정의합니다. C# 프로그램은 클래스 기반입니다.
- `static void Main(string[] args)`
    
    - 프로그램의 시작점을 의미하는 Main 메서드를 정의합니다. 모든 C# 콘솔 응용 프로그램에는 Main 메서드가 필요합니다.

이후의 코드는 위에서 설명한대로 사용자로부터 두 개의 숫자를 입력받아 합산 결과를 출력합니다.

**결과:**

- 사용자가 5와 7을 차례로 입력할 경우, 결과는 다음과 같습니다:

```c#
Enter first number:
5
Enter second number:
7
The sum of 5 and 7 is: 12
```

- 콘솔화면에 Enter first number: 입력창이 뜨면 사용자가 숫자를 입력합니다.
- 다음 숫자도 입력하면 결과가 출력 됩니다.

#### **6. 변수와 스코프**

C#에서 변수의 스코프는 변수가 선언된 블록 내에서만 접근 가능하다는 것을 의미합니다. 예를 들어, 메서드 내에서 선언된 변수는 해당 메서드 내에서만 사용할 수 있습니다.

```c#
public void MyMethod()
{
    int localVariable = 10;
}
```

위의 `localVariable`은 `MyMethod` 메서드 내에서만 접근 가능합니다.