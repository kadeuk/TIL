이전 편에서는 문자열의 기본적인 포매팅 방법과 몇몇 중요한 메서드들을 살펴보았습니다. 이번 편에서는 문자열 메서드의 활용법을 더 깊게 알아보며, 문자열 작업에 있어서 유용한 몇 가지 추가 기법을 배워보겠습니다.

### 1. 문자열의 시작과 끝 확인하기

`StartsWith`와 `EndsWith` 메서드를 사용하면 문자열이 특정 문자열로 시작하거나 끝나는지 확인할 수 있습니다.

```c#
using System;

class Program
{
    static void Main()
    {
        string text = "Hello, World!";
        Console.WriteLine(text.StartsWith("Hello"));  // true
        Console.WriteLine(text.EndsWith("!"));        // true
    }
}
```

```c#
true
true
```

### 2. 문자열 위치 찾기

`IndexOf` 메서드는 문자열 내에서 다른 문자열의 위치를 찾아 그 시작 인덱스를 반환합니다. 만약 문자열이 없으면 `-1`을 반환합니다.

```c#
using System;

class Program
{
    static void Main()
    {
        string text = "I love C# programming!";
        int index = text.IndexOf("C#");
        Console.WriteLine(index); // 7
    }
}
```

```c#
7
```

### 3. 문자열 대소문자 변경

`ToUpper`와 `ToLower` 메서드를 사용하여 문자열의 대소문자를 변경할 수 있습니다

```c#
using System;

class Program
{
    static void Main()
    {
        string text = "Hello, World!";
        Console.WriteLine(text.ToUpper());  // HELLO, WORLD!
        Console.WriteLine(text.ToLower());  // hello, world!
    }
}
```

```c#
HELLO, WORLD!
hello, world!
```

문자열 메서드는 문자열 처리 작업에서 굉장히 중요합니다. 문자열 메서드를 잘 활용하면 다양한 문자열 처리 작업을 훨씬 더 효율적으로 수행할 수 있습니다. 다음 편에서는 문자열 외의 다른 데이터 타입과 그에 관련된 기본 연산자에 대해 배워보겠습니다!