#좋아하는 운동 종목을 리스트에 저장하고 반복문을 이용해서 출력

myFavoriteSports = ['수영','축구','배구','야구','미식축구','농구']
for i in range(len(myFavoriteSports)):
    print('myFavoriteSports[{}] : {}'.format(i, myFavoriteSports[i]))


for item in myFavoriteSports:
    print(item)


n = 0
while n < len(myFavoriteSports):
    print(myFavoriteSports[n])
    n += 1