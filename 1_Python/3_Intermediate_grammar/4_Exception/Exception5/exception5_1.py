try:
    inputData = input('inputNumber : ')
    numInt = int(inputData)

except:
    print('exception raise')
    print('not number')
else:
    if numInt % 2 == 0:
        print('evenNumber')
    else:
        print('odd number')
finally:
    print(f'inputData : {inputData}')