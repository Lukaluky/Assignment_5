from abc import ABC, abstractmethod

# Base class for weapons
class Weapon:
    def __init__(self, type, damage, speed, range):
        self.type = type
        self.damage = damage
        self.speed = speed
        self.range = range

    def __str__(self):
        return f"Type: {self.type}, Damage: {self.damage}, Speed: {self.speed}, Range: {self.range}"

# Base class for game characters
class Character:
    def __init__(self, name, char_class, weapon, health, mana):
        self.name = name
        self.char_class = char_class
        self.weapon = weapon
        self.health = health
        self.mana = mana

    def __str__(self):
        return (f"Name: {self.name}, Class: {self.char_class}, "
                f"Weapon: {self.weapon}, Health: {self.health}, Mana: {self.mana}")

# Abstract factory for creating characters and weapons
class CharacterFactory(ABC):
    @abstractmethod
    def create_character(self, name):
        pass

    @abstractmethod
    def create_weapon(self):
        pass

# Concrete factory for Warrior with Sword
class WarriorSwordFactory(CharacterFactory):
    def create_character(self, name):
        weapon = self.create_weapon()
        return Character(name, "Warrior", weapon, health=200, mana=50)

    def create_weapon(self):
        return Weapon("Sword", damage=50, speed=2, range=1)

# Concrete factory for Mage with Staff
class MageStaffFactory(CharacterFactory):
    def create_character(self, name):
        weapon = self.create_weapon()
        return Character(name, "Mage", weapon, health=100, mana=200)

    def create_weapon(self):
        return Weapon("Staff", damage=30, speed=3, range=3)

# Concrete factory for Archer with Bow
class ArcherBowFactory(CharacterFactory):
    def create_character(self, name):
        weapon = self.create_weapon()
        return Character(name, "Archer", weapon, health=120, mana=75)

    def create_weapon(self):
        return Weapon("Bow", damage=40, speed=4, range=5)

# Class to use factories to create game characters
class CharacterCreator:
    def __init__(self, factory=None):
        self.factory = factory

    def set_factory(self, factory):
        self.factory = factory

    def create_character(self, name):
        return self.factory.create_character(name)

# Main function to demonstrate character creation
def main():
    character_creator = CharacterCreator()

    # Create a Warrior with a Sword
    character_creator.set_factory(WarriorSwordFactory())
    warrior = character_creator.create_character("Arthur")
    print(warrior)

    # Create a Mage with a Staff
    character_creator.set_factory(MageStaffFactory())
    mage = character_creator.create_character("Merlin")
    print(mage)

    # Create an Archer with a Bow
    character_creator.set_factory(ArcherBowFactory())
    archer = character_creator.create_character("Robin")
    print(archer)

if __name__ == "__main__":
    main()
