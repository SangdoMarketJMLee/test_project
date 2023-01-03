uri = './'

with open(uri + 'lans.txt','r') as f:
    lanList = f.readlines()

print(f'lanList : {lanList}')
print(f'lanList type : {type(lanList)}')