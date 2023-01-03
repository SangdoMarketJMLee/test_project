# 다음은 전쟁에서 사용되는 암호이다. 암호를 해독하는 프로그램을 만들어라

secret = '27156231'
secretList = []
solvedList = ''
for cha in secret:
    secretList.append(int(cha))

secretList.reverse()
print(secretList)

val = secretList[0] * secretList[1]
secretList.insert(2,val)
val = secretList[3] * secretList[4]
secretList.insert(5,val)
val = secretList[6] * secretList[7]
secretList.insert(8,val)
val = secretList[9] * secretList[10]
secretList.insert(11,val)

print(secretList)
