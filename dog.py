from animal import Animal

class Dog(Animal):
    """
    Derived class representing a dog, which is a type of Animal.
    """
    def __init__(self, name, species, breed):
        """
        Initializes a Dog instance with name, species, and breed.
        """
        super().__init__(name, species)  # Initialize the Animal class with name and species
        self.breed = breed  # Initialize breed specific to the Dog class

    def speak(self):
        """
        Outputs a specific message for dogs.
        """
        print("The dog barks.")

    def __str__(self):
        """
        String representation of the Dog object.
        """
        return f"Kingdom: '{self.kingdom}', Name: '{self.name}', Species: '{self.species}', Breed: '{self.breed}'"
