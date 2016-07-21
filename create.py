"""Creates Cats & Dogs"""
import random
import names


class AbstractAnimal(object):
    """The idea of an animal"""

    def __init__(self, name):
        self.name = name
        self.age = random.randrange(1, 15)
        self.obedience_level = random.randrange(0, 10)
        self.hunger = random.randrange(0, 10)
        self.cranky = random.randrange(0, 10)
        self.mortal_enemy = []
        self.best_friends = []
        self.spay_or_neuter = False

    def __repr__(self):
        """Provides useful represenation when printed"""

        return """<{} name: {} >""".format(self.species, self.name)

    def __add__(self, other):
        """What happens when you add two animals"""

        if self.cranky > 7:
            self.mortal_enemy.append(other)

            return"{} is {} mortal enemy".format(other.name, self.name)

        self.best_friends.append(other)

        return "{} is {} best friend".format(other.name, self.name)

    def __sub__(self, other):
        """What happens when you subtract two animals"""


    def __mul__(self, other):
        """What happens when you multiply two animals"""

        if self.species != other.species:
            return "nope"

        if self.spay_or_neuter is True or other.spay_or_neuter is True:
            return "cannot multiply {} due to animal being spayed/neutered".format((self.species + 's'))

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

    def undergo_spay_or_neuter(self):
        """Spays or neuters animal"""

        self.spay_or_neuter = True


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
