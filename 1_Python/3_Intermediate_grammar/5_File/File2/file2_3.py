# 텍스트 파일에서 Python을 파이썬으로 변경해서 파일에 다시 저장
file = open('./about_python.txt','r')
str = file.read()

print(f'str : {str}')
file.close()

str = str.replace('Python','파이썬',2)
print(f'str : {str}')

file = open('./about_python.txt','w+')

strCnt = file.write(str)

file.close()
