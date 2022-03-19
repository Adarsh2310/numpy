#wihtout parameter
'''class Mob:
    def __init__(self):
        print('mobile construt')
sam=Mob()'''
#Without Parameter
class Mob():
    def __init__(self,m,v=60):
        self.model=m
        self.volume=v
    def show_model(self,p):
        price=p
        print("Models:",self.model,"Price:",price)
        print("volume:",self.volume)
sam=Mob('samung')
sam.show_model(13444)



