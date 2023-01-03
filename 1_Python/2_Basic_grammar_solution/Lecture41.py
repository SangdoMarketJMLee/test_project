name = '홍길동'
productName = '야구글러브'
productNumber = '2568956'
payMethod = '신용카드'
productPrice = 110000
payPrice = 100000
point = 10000
date = '2021/08/03 21:50:12'
installment = '6개월'
installmentMethod = '무'
callNum = '02-1234-5678'

print(name+' 고객님 안녕하세요')
print(name+' 고객님의 주문이 완료되었습니다.')
print('다음은 주문건에 대한 상세내역입니다.')
print('-'*25)
print('상품명 : {}'.format(productName))
print('주문번호 : {}'.format(productNumber))
print('결제방법 : {}'.format(payMethod))
print('상품금액 : {} 원'.format(productPrice))
print('결제금액 : {} 원'.format(payPrice))
print('결제일시 : {}'.format(date))
print('할부 : {} 개월'.format(installment))
print('할부유형 : {} 개월'.format(installmentMethod))
print('문의 : {}'.format(callNum))
print('-'*25)
print('저희 사이트를 이용해 주셔서 감사합니다')

