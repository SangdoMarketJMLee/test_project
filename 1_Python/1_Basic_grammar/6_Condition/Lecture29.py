exampleScore = int(input('점수 입력 : '))
if exampleScore < 60:
    print('재시험 대상 입니다.')
else:
    if exampleScore >= 90:
        print('A')
    elif exampleScore >=80:
        print('B')
    elif exampleScore >=70:
        print('C')
    elif exampleScore >=60:
        print('D')

selectNum = int(input('출퇴근 대상자 인가요? 1.Yes \t 2.No'))

if selectNum == 1:
    print('교통 수단을 선택하세요')
    trans = int(input('1. 도보, 자전거 \t 2. 버스, 지하철 \t 3. 자가용'))
    if trans == 1:
        print('세금 감면 5%')
    elif trans == 2:
        print('세금 감면 3%')
    elif trans == 3:
        print('추가 세금 1%')

elif selectNum == 2:
    print('세금 변동 없습니다.')
else:
    print('잘못 입력 했습니다.')