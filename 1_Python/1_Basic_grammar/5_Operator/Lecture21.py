char1 = 'A'
char2 = 'S'

print('\'{}\' > \'{}\' :{}'.format(char1,char2,(char1 > char2)))
print('\'{}\' > \'{}\' :{}'.format(char1,char2,(char1 >= char2)))
print('\'{}\' > \'{}\' :{}'.format(char1,char2,(char1 < char2)))
print('\'{}\' > \'{}\' :{}'.format(char1,char2,(char1 <= char2)))
print('\'{}\' > \'{}\' :{}'.format(char1,char2,(char1 == char2)))
print('\'{}\' > \'{}\' :{}'.format(char1,char2,(char1 != char2)))

print('\'A\' -> {}'.format(ord('A')))
print('\'S\' -> {}'.format(ord('S')))
print('65 -> {}'.format(chr(65)))
print('83 -> {}'.format(chr(83)))

userInputAlphabet = input('알파벳 입력 : ')
print('{} : {}'.format(userInputAlphabet,ord(userInputAlphabet)));
userInputASCII = int(input('아스키 코드 입력 : '))
print('{} : {}'.format(userInputASCII,chr(userInputASCII)))

systemID = '123@gamil.com'
systemPW = '12345678'

userInputId = input('아이디 입력 : ')
userInputPw = input('패스워드 입력 : ')

print('아이디 비교 결과 : {}'.format(systemID == userInputId))
print('아이디 비교 결과 : {}'.format(systemPW == userInputPw))