"""Creates Cats & Dogs"""
import random
import names


class AbstractAnimal(object):
    """The idea of an animal"""

    def __init__(self, name):
        self.name = name
        self.age = random.randrange(1, 15)
        self.obedience_level = random.randrange(1, 15)
        self.hunger = random.randrange(0, 10)

    def __repr__(self):
        """Provides useful represenation when printed"""

        return """<Cat name: {} >""".format(self.name)

    def __add__(self, other):
        """What happens when you add two animals"""

        if self.species != other.species:
            return "nope"

        litter_size = random.randrange(0, 5)
        litter = []
        for baby in range(litter_size):
            b = Cat(names.get_first_name())
            b.age = 0
            litter.append(b)

        return litter

    def speak(self):
        print "%s, I'm %s the %s" % (
            self.greet, self.name, self.species)


class Cat(AbstractAnimal):
    """A Cat"""

    greet = "Meow"
    species = "cat"

    def __init__(self, name):
        super(Cat, self).__init__(name)
        self.purr_level = random.randrange(0, 10)


class Dog(AbstractAnimal):
    """A Dog"""

    greet = "Woof"
    species = "dog"

    def __init__(self, name):
        self.loyality_level = random.randrange(0, 10)
        super(Dog, self).__init__(name)
