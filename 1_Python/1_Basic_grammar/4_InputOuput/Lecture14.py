userName = '홍길동'
userAge = 20
print('userName : {}'.format(userName))
print('userAge : {}'.format(userAge))
print('userName : {} , userAge : {}'.format(userName,userAge))

print('나의 이름은 {}이고, 나이는 {}살 입니다. {} 이름은 아버님께서 지어 주셨습니다'.format(userName,userAge,userName))
print('나의 이름은 {0}이고, 나이는 {1}살 입니다. {0} 이름은 아버님께서 지어 주셨습니다'.format(userName,userAge))

print('userName : %s' % userName)
print('userAge : %d' % userAge)
print('userName : %s, userAge : %d' % (userName,userAge))

print('Pi : %f' % 3.14)
print('Pi : %d' % 3.14)

print('Pi : %.0f' % 3.141592)
print('Pi : %.2f' % 3.141592)
print('Pi : %.4f' % 3.141592)
print('Pi : %.6f' % 3.141592)

radius = int(input('반지름 입력 : '))
pi = float(input('원주율 입력 : '))

print('radius : {}'.format(radius))
print('pi : {}'.format(pi))
print('radius : %.1f , pi : %f' %(radius,pi))
print('radius : %.6f , pi : %.6f' %(radius,pi))
print('radius : %.2f , pi : %.2f' %(radius,pi))