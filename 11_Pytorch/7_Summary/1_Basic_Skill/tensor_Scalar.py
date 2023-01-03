import torch
# 스칼라는 상수값 -> 하나의 값을 표현 할때 1개의 수치로 표현한것
scalar1 = torch.tensor([1.])
print(f'scalar1 : {scalar1}')

scalar2 = torch.tensor([3.])
print(f'scalar2 : {scalar2}')

# 사칙연산을 이용하여 계산가능
add_scalar = scalar1 + scalar2
print(f'add_scalar : {add_scalar}')

sub_scalar = scalar1 - scalar2
print(f'sub_scalar : {sub_scalar}')

mul_scalar = scalar1 * scalar2
print(f'mul_scalar : {mul_scalar}')

div_scalar = scalar1 / scalar2
print(f'div_scalar : {div_scalar}')

# 내장된 메서드 사용 가능

torch_scalar_add = torch.add(scalar1,scalar2)
print(f'torch_add : {torch_scalar_add}')

torch_scalar_sub = torch.sub(scalar1,scalar2)
print(f'torch_sub : {torch_scalar_sub}')

torch_scalar_mul = torch.mul(scalar1,scalar2)
print(f'torch_mul : {torch_scalar_mul}')

torch_scalar_div = torch.div(scalar1,scalar2)
print(f'torch_div : {torch_scalar_div}')
