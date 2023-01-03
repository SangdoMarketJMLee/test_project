languages = ['c/c++','java','c#','python','javascript']

uri = './'
for item in languages:
    with open(uri + 'languages.txt','a') as f:
        f.write(item)
        f.write('\n')


