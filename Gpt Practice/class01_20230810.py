# 기본적인 클래스 생성
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
person1 = Person('철수', 25)
print(person1.name)
print(person1.age)

# 도서 정보를 저장하는 클래스 생성

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
book1 = Book('Gpt', 'Gpt')
print(book1.title)
print(book1.author)

# 은행 계좌 클래스 생성

class BankAccount():
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            print('잔액이 부족합니다')
            return
        self.balance -= amount
        return self.balance
    
account = BankAccount()
account.deposit(1000)
print(account.balance)

account.withdraw(500)
print(account.balance)

account.withdraw(600)
print(account.balance)

# 학생 정보 관리

class Student():
    def __init__(self, name='', grade = ''):
        self.name = name
        self.grade = grade
    
    def show_info(self):
        print(f'이 학생의 이름은 {self.name}이고 학년은 {self.grade} 입니다')

student2 = Student('철수', '2학년')
student2.show_info()

# 도서 대출 관리

class Book():
    def __init__(self, title, is_borrowed=False):
        self.title = title
        self.is_borrowed = is_borrowed

    def borrow(self):
        self.is_borrowed = True
        print(f'{self.title}책이 대출되었습니다.')
    
    def return_book(self):
        self.is_borrowed = False
        print('책이 반납되었습니다.')

    def show_status(self):
        if self.is_borrowed:
            print(f'"{self.title}" 책은 대출중입니다')
        else:
            print(f'"{self.title}" 책은 대출 가능합니다')   
book3 = Book('Gpt에대하여')
book3.borrow()
book3.show_status()

