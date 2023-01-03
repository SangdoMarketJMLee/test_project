uri = './'

with open(uri + 'lans.txt','r') as f:
    line = f.readline()

    while line != '':
        print(f'line : {line}',end='')
        line = f.readline()



