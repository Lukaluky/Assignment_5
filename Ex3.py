from abc import ABC, abstractmethod


# Base class for all furniture products
class Furniture:
    def __init__(self, name, style, material, price):
        self.name = name
        self.style = style
        self.material = material
        self.price = price

    def __str__(self):
        return f"{self.name}: Style={self.style}, Material={self.material}, Price=${self.price:.2f}"


# Abstract Factory Class
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_table(self):
        pass

    @abstractmethod
    def create_sofa(self):
        pass


# Concrete Factory for Modern Wood furniture
class ModernWoodFactory(FurnitureFactory):
    def create_chair(self):
        return Furniture("Modern Chair", "Modern", "Wood", 120.0)

    def create_table(self):
        return Furniture("Modern Table", "Modern", "Wood", 210.0)

    def create_sofa(self):
        return Furniture("Modern Sofa", "Modern", "Wood", 500.0)


# Concrete Factory for Traditional Metal furniture
class TraditionalMetalFactory(FurnitureFactory):
    def create_chair(self):
        return Furniture("Traditional Chair", "Traditional", "Metal", 100.0)

    def create_table(self):
        return Furniture("Traditional Table", "Traditional", "Metal", 180.0)

    def create_sofa(self):
        return Furniture("Traditional Sofa", "Traditional", "Metal", 450.0)


# Concrete Factory for Industrial Glass furniture
class IndustrialGlassFactory(FurnitureFactory):
    def create_chair(self):
        return Furniture("Industrial Chair", "Industrial", "Glass", 150.0)

    def create_table(self):
        return Furniture("Industrial Table", "Industrial", "Glass", 250.0)

    def create_sofa(self):
        return Furniture("Industrial Sofa", "Industrial", "Glass", 550.0)


# Class to use factories to create furniture
class FurnitureCreator:
    def __init__(self, factory=None):
        self.factory = factory

    def set_factory(self, factory):
        self.factory = factory

    def create_chair(self):
        return self.factory.create_chair()

    def create_table(self):
        return self.factory.create_table()

    def create_sofa(self):
        return self.factory.create_sofa()


# Main function demonstrating the usage
def main():
    # User selects Modern Wood furniture
    furniture_creator = FurnitureCreator(ModernWoodFactory())

    chair = furniture_creator.create_chair()
    table = furniture_creator.create_table()
    sofa = furniture_creator.create_sofa()

    print(chair)
    print(table)
    print(sofa)

    # Change to Traditional Metal furniture
    furniture_creator.set_factory(TraditionalMetalFactory())
    chair = furniture_creator.create_chair()
    table = furniture_creator.create_table()
    sofa = furniture_creator.create_sofa()

    print(chair)
    print(table)
    print(sofa)


if __name__ == "__main__":
    main()
