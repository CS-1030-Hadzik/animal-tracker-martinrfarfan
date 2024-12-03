from animal import Animal
from dog import Dog

if __name__ == "__main__":
    # TODO: Create an instance of the Animal class
    animal = Animal(name="Generic", species="Unknown")
   
    # TODO: Print the Animal instance
    print(animal)
  
    # TODO: Call the method to make a generic animal sound
    animal.speak()

    # TODO: Create an instance of the Dog class
    dog = Dog(name="Buddy", species="Canine", breed="Golden Retriever")

    # TODO: Print the Dog instance
    print(dog)

    # TODO: Call the method to make the dog-specific sound
    dog.speak()
   
    # TODO print out all the animals
    print("\nAll animals:")
    for a in Animal.all_animals:
        print(a)
   