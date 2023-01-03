import torch
# Vector -> 하나의 값을 2개 이상의 수치로 표현한 것
vector1 = torch.tensor([1.,2.,3.])
print(f'vector1 : {vector1}')

vector2 = torch.tensor([4.,5.,6.])
print(f'vector2 : {vector2}')

# 사칙연산을 이용해 계산할 수 있으며 각 요소별로 연산된다
add_vector = vector1 + vector2
print(f'add_vector : {add_vector}')

sub_vector = vector1 - vector2
print(f'sub_vector : {sub_vector}')

mul_vector = vector1 * vector2
print(f'mul_vector : {mul_vector}')

div_vector = vector1 / vector2
print(f'div_vector : {div_vector}')

# 내재된 사칙연산 메서드를 이용해 계산할 수 있다.

torch_vector_add = torch.add(vector1,vector2)
print(f'torch_vector_add : {torch_vector_add}')

torch_vector_sub = torch.sub(vector1,vector2)
print(f'torch_vector_sub : {torch_vector_sub}')

torch_vector_mul = torch.mul(vector1,vector2)
print(f'torch_vector_mul : {torch_vector_mul}')

torch_vector_div = torch.div(vector1,vector2)
print(f'torch_vector_div : {torch_vector_div}')


