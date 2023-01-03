def greet():
    print('안녕하세요')
greet()

def greet1(customer):
    print(f'{customer} 고객님 안녕하세요!')
greet1('홍길동')

def addFun(n1,n2):
    print(f'{n1} + {n2} = {n1+n2}')

addFun(1,3)

def printNumber(*numbers):
    for number in numbers:
        print(number, end='')
    print()

printNumber(1,2,10)

def printScore(kor, eng, mat):
    sum = kor+eng+mat
    avg = sum/3
    print(f'총점 : {sum}')
    print(f'평균 : {round(avg,2)}')

korScore = int(input('국어 점수 입력: '))
engScore = int(input('영어 점수 입력: '))
matScore = int(input('수학 점수 입력: '))

printScore(korScore,engScore,matScore)