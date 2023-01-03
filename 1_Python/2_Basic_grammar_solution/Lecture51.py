speed = int(input('속도 입력 : '))
if speed < 50:
    print('안전 속도 준수!')
elif speed > 50:
    print('안전속도 위반!! 과태료 50,000원 부과 대상')

text = input('메시지 입력 : ')
textLength = len(text)

if textLength < 50:
    print('SMS 발송')
    print('메시지 길이 : {}'.format(textLength))
    print('메시지 발송 요금 : 50원')
elif textLength > 50:
    print('SMS 발송')
    print('메시지 길이 : {}'.format(textLength))
    print('메시지 발송 요금 : 100원')