from abc import ABC, abstractmethod

# Supporting Classes for Character Properties
class Ability:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Equipment:
    def __init__(self, name, type):
        self.name = name
        self.type = type

class Attribute:
    def __init__(self, strength, intelligence, agility):
        self.strength = strength
        self.intelligence = intelligence
        self.agility = agility

class Appearance:
    def __init__(self, color, height, build):
        self.color = color
        self.height = height
        self.build = build

# Character Base Class
class Character:
    def __init__(self, name, appearance, abilities, equipment, attributes):
        self.name = name
        self.appearance = appearance
        self.abilities = abilities
        self.equipment = equipment
        self.attributes = attributes

    def display(self):
        print(f"Name: {self.name}")
        print(f"Appearance: {self.appearance.color}, {self.appearance.height}, {self.appearance.build}")
        print("Attributes: Str={}, Int={}, Agi={}".format(self.attributes.strength,
                                                          self.attributes.intelligence,
                                                          self.attributes.agility))
        for ability in self.abilities:
            print(f"Ability: {ability.name} - {ability.description}")
        for equipment in self.equipment:
            print(f"Equipment: {equipment.name} ({equipment.type})")

# Abstract Factory Class
class CharacterFactory(ABC):
    @abstractmethod
    def create_character(self, name):
        pass

# Concrete Factory Classes
class WarriorFactory(CharacterFactory):
    def create_character(self, name):
        return Character(
            name=name,
            appearance=Appearance("Red", "Tall", "Muscular"),
            abilities=[Ability("Slash", "A powerful sword attack")],
            equipment=[Equipment("Sword", "Weapon")],
            attributes=Attribute(10, 4, 6)
        )

class MageFactory(CharacterFactory):
    def create_character(self, name):
        return Character(
            name=name,
            appearance=Appearance("Blue", "Medium", "Slim"),
            abilities=[Ability("Fireball", "A fiery explosive spell")],
            equipment=[Equipment("Staff", "Weapon")],
            attributes=Attribute(3, 10, 7)
        )

class ArcherFactory(CharacterFactory):
    def create_character(self, name):
        return Character(
            name=name,
            appearance=Appearance("Green", "Short", "Lean"),
            abilities=[Ability("Piercing Arrow", "A long-range arrow strike")],
            equipment=[Equipment("Bow", "Weapon")],
            attributes=Attribute(6, 5, 9)
        )

# Character Creation System
class CharacterCreator:
    def __init__(self, factory=None):
        self.factory = factory

    def set_factory(self, factory):
        self.factory = factory

    def create_character(self, name):
        return self.factory.create_character(name)

# Main function to run the game
def main():
    creator = CharacterCreator(WarriorFactory())
    warrior = creator.create_character("Aragon")
    warrior.display()

    creator.set_factory(MageFactory())
    mage = creator.create_character("Gandalf")
    mage.display()

    creator.set_factory(ArcherFactory())
    archer = creator.create_character("Legolas")
    archer.display()

if __name__ == "__main__":
    main()
