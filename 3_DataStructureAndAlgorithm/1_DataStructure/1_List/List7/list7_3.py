message = input('메시지 입력 : ')
cnt = 0
for idx, value in enumerate(message):
    if value == ' ':
        cnt +=1

print('공백 개수 : {}'.format(cnt))