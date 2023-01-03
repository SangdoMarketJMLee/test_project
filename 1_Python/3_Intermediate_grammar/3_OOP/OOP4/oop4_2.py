plaOriSco = [8.7,9.1,8.9,9.0,7.9,9.5,8.8,8.3]
plaCopSco = plaOriSco.copy()

plaOriSco.sort()

plaCopSco.sort()
plaCopSco.pop(0)
plaCopSco.pop()

print(f'plaOriSco : {plaOriSco}')
print(f'plaCopSco : {plaCopSco}')

oriTot = round(sum(plaOriSco),2)
oriAvg = round(oriTot / len(plaOriSco),2)

print(f'oriTot : {oriTot}')
print(f'oriAvg : {oriAvg}')

copTot = round(sum(plaCopSco),2)
copAvg = round(copTot/len(plaCopSco),2)

print(f'copTot : {copTot}')
print(f'copAvg : {copAvg}')

print(f'oriAvg - copAvg : {oriAvg - copAvg}')