languages = ['c/c++','java','c#','python','javascript']

uri = './'

with open(uri + 'languages.txt','a') as f:
    f.writelines(languages)

