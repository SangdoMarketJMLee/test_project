sports = ['농구','수구','축구','마라톤','테니스']

for i in range(len(sports)):
    print('{} : {}'.format(i, sports[i]))

print('-'*40)
for idx, value in enumerate(sports):
    print('{} : {}'.format(idx, value))