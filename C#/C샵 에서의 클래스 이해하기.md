C#은 객체 지향 프로그래밍 언어로, 여기서 "객체 지향"이란 현실 세계의 객체를 프로그램으로 모델링하여 구현하는 방식을 의미한다. 이러한 객체 지향의 핵심 요소 중 하나가 바로 '클래스'이다.

### 클래스(Class)란?

클래스는 객체를 생성하기 위한 틀 또는 설계도로 생각할 수 있다. 클래스에는 데이터와 함수가 포함되어 있으며, 이를 통해 객체의 상태와 행동을 정의한다.

### 예제로 클래스 이해하기

```c#
public class Dog
{
    // 속성(데이터)
    public string Name { get; set; }
    public int Age { get; set; }

    // 생성자
    public Dog(string name, int age)
    {
        Name = name;
        Age = age;
    }

    // 메서드(행동)
    public void Bark()
    {
        Console.WriteLine($"{Name}가 멍멍하고 짖습니다.");
    }
}
```

1. **클래스 선언**: `public class Dog`는 `Dog`라는 이름의 클래스를 정의한다.
2. **속성**: `Name`과 `Age`는 각각 개의 이름과 나이를 나타내는 속성이다. `public string Name { get; set; }`는 Name이라는 문자열 속성을 정의하며, get과 set을 통해 값을 가져오거나 설정할 수 있다.
3. **생성자**: `public Dog(string name, int age)`는 Dog 클래스의 객체가 생성될 때 호출되는 생성자이다. 생성자는 객체의 초기 상태를 설정하는 데 사용된다.
4. **메서드**: `Bark()` 메서드는 개가 짖는 행동을 나타낸다. 메서드는 클래스의 행동을 나타내며, 해당 클래스의 객체에서 호출할 수 있다.
### 클래스 사용하기

```c#
class Program
{
    static void Main(string[] args)
    {
        Dog myDog = new Dog("Max", 3);
        myDog.Bark();
    }
}
```


- `Dog myDog = new Dog("Max", 3);`: `Dog` 클래스의 새로운 인스턴스(객체)를 생성하고 그 인스턴스를 `myDog` 변수에 할당한다. 이때 "Max"와 3이 생성자에 전달된다.
- `myDog.Bark();`: `myDog` 객체의 `Bark()` 메서드를 호출한다. 결과적으로 "Max가 멍멍하고 짖습니다."라는 문장이 출력된다.

C#의 클래스는 객체 지향 프로그래밍의 중심적인 요소 중 하나이다. 클래스를 통해 현실 세계의 개체를 효과적으로 모델링하고, 그 개체의 속성과 행동을 코드에 반영할 수 있다. 클래스를 잘 이해하고 활용하면, 더 효율적이고 가독성 높은 코드를 작성할 수 있다