class Pokemon:
    def __init__(self, name, hp):
        self.name  = name
        self.hp = hp
        self.type = type

pikachu = Pokemon(name:"Pikachu", hp:100, type:"Electric")
squirtle = Pokemon(name:"squirtle", hp:200, type:"Water")
print(pikachu.type)
print(squirtle.hp)