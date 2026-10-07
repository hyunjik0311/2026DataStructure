class Pokemon:
    # def __init__(self, name, hp, type):
    def __init__(self, name, hp, type=None): # default parameter 값으로 None 할당
        self.name  = name
        self.hp = hp
        self.type = type

pikachu = Pokemon( ame:"Pikachu", hp:100, type:"Electric")
squirtle = Pokemon(name:"Squirtle", hp:200, type:"Water")
charmander = Pokemon(name:"Charmander", hp:150, type:"Fire") # default parameter 안쓰면 error
print(pikachu.type)
print(squirtle.hp)