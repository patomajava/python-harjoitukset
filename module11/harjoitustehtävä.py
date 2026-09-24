class Adventurer():
    def __init__(self, name):
        self.name = name
        self.healthPoints = 100
        self.stamina = 100
        self.attackDamage = 10

    def gain_life(self, amount):
        self.healthPoints += amount
        print(f"{self.name} gained {amount} health points.")

    def lose_life(self, amount, condition):
        if self.healthPoints - amount < 0:
            self.healthPoints = 0
        else:
            self.healthPoints -= amount
            print(f"{self.name}: Lost {amount} health points because {condition}.")


class Party():
    def __init__(self):
        self.adventurers = []

    def add_member(self, player):
        self.adventurers.append(player)

    def retire_member(self, player):
        self.adventurers.remove(player)

    def show_members(self):
        print("\nCurrent Players:")
        for player in self.adventurers:
            print(player.name)

    def show_health(self):
        print("\nCurrent Players and their Health Points:")
        for player in self.adventurers:
            print(f"{player.name}: {player.healthPoints} hp")


class Mage(Adventurer):
    def __init__(self, name):
        super().__init__(name)
        self.healthPoints = 50
        self.attackDamage = 20

    def party_heal(self):
        for player in party.adventurers:
            player.healthPoints += 50

class Paladin(Adventurer):
    def __init__(self, name):
        super().__init__(name)
        self.healthPoints = 150
        self.attackDamage = 5

class Rogue(Adventurer):
    def __init__(self, name):
        super().__init__(name)

party = Party()

player_paladin_01 = Paladin("Paladin1")
player_mage_01 = Mage("Mage1")
player_rogue_01 = Rogue("Rogue1")

party.add_member(player_paladin_01)
party.add_member(player_mage_01)
party.add_member(player_rogue_01)

party.show_health()
print("")

player_paladin_01.lose_life(100, "he got hit in the head by a goblin")
player_mage_01.lose_life(20, "he ate a poison mushroom")
player_rogue_01.lose_life(50, "he fell down a tree")

player_mage_01.party_heal()
party.retire_member(player_mage_01)
party.show_health()