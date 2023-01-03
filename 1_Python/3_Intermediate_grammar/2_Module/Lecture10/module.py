import Calculator

Calculator.add(20,10)
Calculator.sub(20,10)
Calculator.mul(20,10)
Calculator.div(20,10)

import LottoMachine

lottoNumbers = LottoMachine.getLottoNumbers()
print(f'lottoNumbers: {lottoNumbers}')

import ReverseStr

userInputStr = input('문자열 입력 :')

reversedString = ReverseStr.reverseStr(userInputStr)

print(f'reversedString: {reversedString}')