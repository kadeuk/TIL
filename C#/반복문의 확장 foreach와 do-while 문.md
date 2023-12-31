반복문의 확장에는 여러 가지가 있지만, 여기서는 `foreach`와 `do-while`에 대해 중점적으로 알아보겠습니다. 이 두 반복문은 특정한 상황에서 유용하게 사용됩니다.

### foreach 문

`foreach`문은 컬렉션 또는 배열의 각 요소에 대해 반복을 수행합니다. 주로 배열이나 리스트 같은 컬렉션의 모든 요소를 차례대로 접근할 때 사용합니다.

```c#
string[] fruits = { "사과", "바나나", "체리" };

foreach (string fruit in fruits)
{
    Console.WriteLine(fruit + "를 먹습니다.");
}
```

```c#
사과를 먹습니다.
바나나를 먹습니다.
체리를 먹습니다.
```

- `fruits`는 문자열 배열로, 3개의 과일 이름을 담고 있습니다.
- `foreach`문을 사용하여 `fruits` 배열의 모든 요소를 차례대로 접근하며 출력하였습니다.

### do-while 문

`do-while`문은 조건을 검사하기 전에 코드 블록을 최소 한 번 실행하고, 그 후 조건이 참인 동안 계속해서 코드 블록을 실행합니다.

```c#
int k = 0;

do
{
    Console.WriteLine(k + "번째 반복입니다.");
    k++;
} while (k < 2);
```

```c#
0번째 반복입니다.
1번째 반복입니다.
```

- `do` 블록 내의 코드는 최소 한 번 실행됩니다.
- 그 후 `k < 2` 조건을 검사하여 조건이 참인 경우 반복을 계속합니다.
- 위 예제에서는 0부터 1까지 총 2번 반복됩니다.

이번 편에서는 `foreach`와 `do-while` 반복문에 대해 배웠습니다. 각각의 반복문은 특정한 상황에서 더 유용하게 사용될 수 있습니다. 다음 편에서는 C#에서의 배열과 리스트에 대해 알아보겠습니다.