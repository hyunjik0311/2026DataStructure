class Pokemon:
    # def __init__(self, name, hp, type):
    def __init__(self, hp, type, name=None): # default parameter 값으로 None 할당
        self.name  = name
        self.hp = hp
        self.type = type

pikachu = Pokemon(hp:100, type:"Electric", name:"피카츄")
squirtle = Pokemon(hp:200, type:"Water", name:"꼬부기")
charmander = Pokemon(hp:150, type:"Fire", name:"파이리") # default parameter 안쓰면 error
print(charmander.name) # default parameterf로 할당된 None 출력
print(pikachu.type)
print(squirtle.hp)