class Pokemon:
    # def __init__(self, name, hp, type):
    def __init__(self, name, hp, type=None): # default parameter 값으로 None 할당
        self.name  = name
        self.hp = hp
        self.type = type

pikachu = Pokemon("Pikachu", 100, "Electric")
squirtle = Pokemon("Squirtle", 200, "Water")
charmander = Pokemon("Charmander", 150, "Fire") # default parameter 안쓰면 error
print(pikachu.type)
print(squirtle.hp)