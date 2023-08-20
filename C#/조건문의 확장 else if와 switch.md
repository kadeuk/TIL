### else if 문

우리가 만약 다양한 조건들을 체크해야 할 때 `else if`를 사용할 수 있습니다. `if` 문의 조건이 거짓일 때 다음 조건을 확인하여 그 조건이 참인 경우 해당 블록의 코드를 실행합니다.

```c#
int number = 5;

if (number == 3)
{
    Console.WriteLine("number는 3입니다.");
}
else if (number == 5)
{
    Console.WriteLine("number는 5입니다.");
}
else
{
    Console.WriteLine("number는 3도 5도 아닙니다.");
}
```

```c#
number는 5입니다.
```

- `number` 변수에 5라는 값을 할당하였습니다.
- 첫 번째 조건 `number == 3`는 거짓입니다. 따라서 `else if` 문의 조건 `number == 5`를 확인합니다.
- `number == 5`는 참이므로 "number는 5입니다."라는 문장이 출력됩니다.

### switch 문

여러 조건 중 하나가 맞는 경우를 찾을 때 `switch` 문을 사용할 수 있습니다. `switch` 문은 주어진 표현식의 결과와 `case` 레이블의 값을 비교하여 해당 블록의 코드를 실행합니다.

```c#
int day = 3;
switch (day)
{
    case 1:
        Console.WriteLine("월요일입니다.");
        break;
    case 2:
        Console.WriteLine("화요일입니다.");
        break;
    case 3:
        Console.WriteLine("수요일입니다.");
        break;
    default:
        Console.WriteLine("목요일부터 일요일까지의 날짜는 여기에 포함되지 않았습니다.");
        break;
}
```

```c#
수요일입니다.
```

- `day` 변수에 3이라는 값을 할당하였습니다.
- `switch` 문에서 `day`의 값을 체크하여 해당하는 `case` 레이블의 코드를 실행합니다.
- `case 3:`에 해당하는 코드가 실행되어 "수요일입니다."라는 문장이 출력됩니다.

이번 편에서는 조건문의 확장인 `else if`와 `switch` 문에 대해 배웠습니다. 이를 통해 다양한 조건에 따른 코드의 실행을 제어할 수 있게 되었습니다. 다음 편에서는 반복문에 대해 알아볼 것입니다. 프로그램의 흐름을 반복적으로 제어하며 다양한 작업을 수행하는 방법을 배워봅시다!