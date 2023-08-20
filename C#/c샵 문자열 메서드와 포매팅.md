지난 편에서는 문자열의 기본적인 다루는 방법에 대해 배웠습니다. 이번 편에서는 문자열의 다양한 메서드와 문자열 포매팅에 대해 알아보겠습니다.

### 라이브러리 불러오기

먼저, 우리가 사용할 라이브러리를 불러와야 합니다:

```c#
using System;
```

### 1. 문자열 포매팅

문자열 안에서 변수의 값을 동적으로 변경하고 싶을 때, 문자열 포매팅을 사용합니다.

```c#
using System;

class Program
{
    static void Main()
    {
        int age = 25;
        string formattedString = string.Format("나이는 {0}세 입니다.", age);
        Console.WriteLine(formattedString);
    }
}
```

```c#
나이는 25세 입니다.
```

### 2. 문자열 치환

`Replace` 메서드를 사용하여 문자열 내의 특정 문자나 문자열을 다른 문자나 문자열로 치환할 수 있습니다.

```c#
using System;

class Program
{
    static void Main()
    {
        string text = "Hello, Java!";
        string replacedText = text.Replace("Java", "C#");
        Console.WriteLine(replacedText);
    }
}
```

```c#
Hello, C#!
```

### 3. 문자열 분할

`Split` 메서드를 사용하여 문자열을 특정 문자나 문자열을 기준으로 분할할 수 있습니다.

```c#
using System;

class Program
{
    static void Main()
    {
        string text = "apple,banana,grape";
        string[] fruits = text.Split(',');
        foreach (var fruit in fruits)
        {
            Console.WriteLine(fruit);
        }
    }
}
```

```c#
apple
banana
grape
```

문자열은 매우 유연하게 다양한 작업을 수행할 수 있습니다. 이러한 기능들은 여러분의 코드에서 자주 사용되므로 잘 익혀두시기 바랍니다. 다음 편에서는 더 복잡한 문자열 처리 방법과 문자열과 관련된 추가적인 메서드에 대해 살펴보겠습니다