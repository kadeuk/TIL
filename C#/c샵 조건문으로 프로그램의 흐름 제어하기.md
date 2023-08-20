프로그램은 상황에 따라 다른 동작을 수행해야 할 때가 많습니다. 이러한 다양한 상황을 처리하기 위해 조건문을 사용합니다.

### 1. if 문의 기본

#### if 문이란?

`if`문은 주어진 조건이 참인지 거짓인지를 검사하고, 그 결과에 따라 다른 동작을 수행하게 합니다.

```c#
int number = 10;

if (number > 5) {
    Console.WriteLine("number는 5보다 큽니다.");
}
```

```c#
number는 5보다 큽니다.
```

이 코드에서 `number > 5`는 참이기 때문에 `Console.WriteLine` 코드가 실행됩니다.

### 2. else와 else if 사용하기

만약 여러 조건을 검사하고자 한다면 `else if`를 사용합니다. 그리고 조건이 모두 거짓일 때 실행할 코드는 `else` 블록 안에 작성합니다.

```c#
int number = 3;

if (number > 5) {
    Console.WriteLine("number는 5보다 큽니다.");
} else if (number == 5) {
    Console.WriteLine("number는 5와 같습니다.");
} else {
    Console.WriteLine("number는 5보다 작습니다.");
}
```

```c#
number는 5보다 작습니다.
```

### 3. switch 문 사용하기

복잡한 조건들을 검사할 때 `switch` 문을 사용하면 코드가 더 깔끔해집니다.

```c#
char grade = 'B';

switch (grade) {
    case 'A':
        Console.WriteLine("훌륭한 성적입니다.");
        break;
    case 'B':
        Console.WriteLine("좋은 성적입니다.");
        break;
    default:
        Console.WriteLine("성적을 다시 확인해주세요.");
        break;
}
```

```c#
좋은 성적입니다.
```

이번 편에서는 C#에서 조건문의 기본 구조와 사용법에 대해 알아보았습니다. 조건문은 프로그램의 흐름을 제어하는 데 있어 필수적인 도구입니다. 다음 편에서는 반복문을 이용하여 같은 코드를 여러 번 실행하는 방법에 대해 알아보겠습니다