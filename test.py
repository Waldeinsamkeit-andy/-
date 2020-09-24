Class Person:
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def run(self):
        print(f'{self.name}正在疾驰，它是{self.color}的')

benz = Person('奔驰','白色')
benz.run()
