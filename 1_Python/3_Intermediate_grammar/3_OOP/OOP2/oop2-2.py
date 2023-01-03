class NewGenerationPC:
    def __init__(self,name,cpu,memory,ssd):
        self.name = name
        self.cpu = cpu
        self.memory = memory
        self.ssd = ssd

    def doExcel(self):
        print('EXCEL RUN')
    def doPhotoshop(self):
        print('PHOTOSHOP RUN')

    def printPCInfo(self):
        print(f'self.name : {self.name}')
        print(f'self.cpu : {self.cpu}')
        print(f'self.memory : {self.memory}')
        print(f'self.ssd : {self.ssd}')

myPC = NewGenerationPC('intel','i9','128GB','256GB')
myPC.name = 'intelSilver'
myPC.cpu = 'i9'
myPC.memory = '256GB'
myPC.ssd = '512GB'

friendPC = NewGenerationPC('AMD','3500x','128GB','256GB')

myPC.printPCInfo()
friendPC.printPCInfo()