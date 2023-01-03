# 가장 좋아하는 스포츠가 몇 번째에 있는지 출력하는 프로그램을 만들어 보자
sports = ['농구','수구','축구','마라톤','테니스']

favoriteSports = input('가장 좋아하는 스포츠 입력 : ')

for idx, value in enumerate(sports):
    if value == favoriteSports:
        bestSportIdx = idx + 1


print('{} : {}'.format(favoriteSports, bestSportIdx))