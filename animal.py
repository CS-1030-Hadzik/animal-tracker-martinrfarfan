class Animal:
    """
    Base class representing a generic animal.
    """
    # Class-level attribute
    kingdom = "Animalia"
   all_animals = []

    def __init__(self, name, species):
        """
        Initializes an Animal instance with name and species.
        """
        self.name = name
        self.species = species
        # Add each instance to the all_animals list
        Animal.all_animals.append(self)

    def speak(self):
        """
        Outputs a generic message about the animal.
        """
        print("The animal makes a noise.")

    def __str__(self):
        """
        String representation of the Animal object.
        """
        return f"Kingdom: '{self.kingdom}', Name: '{self.name}', Species: '{self.species}'"
