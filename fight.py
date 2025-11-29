class Fight:
    # initiate fight between player and enemy / demon lord being a subclass of enemy
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
    def start_fight(self):
        print(f"The fight between {self.player.name} and {self.enemy.name} begins!")
        while self.player.is_alive() and self.enemy.is_alive():
            self.player.attack(self.enemy)
            if self.enemy.is_alive():
                self.enemy.attack(self.player)
        if self.player.is_alive():
            print(f"{self.player.name} has defeated {self.enemy.name}!")
        else:
            print(f"{self.player.name} has been defeated by {self.enemy.name}!")
class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    def is_alive(self):
        return self.health > 0
    def attack(self, player):
        player.health -= self.attack_power
        print(f"{self.name} attacks {player.name} for {self.attack_power} damage!")
class DemonLord(Enemy):
    def __init__(self):
        super().__init__(name="Demon Lord", health=150, attack_power=25)
class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    def is_alive(self):
        return self.health > 0
    def attack(self, enemy):
        enemy.health -= self.attack_power
        print(f"{self.name} attacks {enemy.name} for {self.attack_power} damage!")
# Example usage:
# player = Player(name="Jarknight", health=100, attack_power=20)
# demon_lord = DemonLord()
# fight = Fight(player, demon_lord)
# fight.start_fight()