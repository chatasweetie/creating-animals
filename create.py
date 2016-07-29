"""Creates Animals"""
import random
import names
import emoji


class AbstractAnimal(object):
    """The idea of an animal"""

    heart = ':heartpulse:'
    sad = ':broken_heart:'
    anger = ':rage:'

    frenemies = ':anguished:'

    def __init__(self, name, species):
        self.name = name
        self.age = random.randrange(1, 15)
        self.obedience_level = random.randrange(0, 10)
        self.hunger = random.randrange(0, 10)
        self.cranky = random.randrange(0, 10)
        self.friendly = random.randrange(0, 10)
        self.mortal_enemy = set()
        self.best_friends = set()
        self.frenemies = set()
        self.spay_or_neuter = False
        self.species = species

    def __repr__(self):
        """Provides useful represenation when printed"""
        print emoji.emojize(self.smile, use_aliases=True)

        return """<{} name: {} >""".format(self.species, self.name)

    def __add__(self, other):
        """What happens when you add two animals"""

        if self.cranky > 7 or self.friendly < 3:
            self.mortal_enemy.add(other)
            print emoji.emojize(self.anger, use_aliases=True)

            return"{} is {} mortal enemy".format(other.name, (self.name + '\'s'))

        self.best_friends.add(other)

        print emoji.emojize(self.smile, use_aliases=True),  emoji.emojize(other.smile, use_aliases=True)

        return "{} is {} best friend".format(other.name, (self.name + '\'s'))

    def __sub__(self, other):
        """What happens when you subtract two animals"""

        if other in self.best_friends:
            self.best_friends.remove(other)
            self.frenemies.add(other)
            print emoji.emojize(self.frenemies, use_aliases=True)
            return"{} is now {} frenemy".format(other.name, (self.name + '\'s'))

        self.mortal_enemy.add(other)

        print emoji.emojize(self.anger, use_aliases=True)
        return"{} is {} mortal enemy".format(other.name, (self.name + '\'s'))


    def __mul__(self, other):
        """What happens when you multiply two animals"""

        if self.species != other.species:
            return "You cannot breed between species"

        if self.spay_or_neuter is True or other.spay_or_neuter is True:
            return "cannot breed {} due to animal being spayed/neutered".format((self.species + 's'))

        print emoji.emojize(self.heart, use_aliases=True) * 2

        litter_size = random.randrange(0, 5)
        litter = []

        for baby in range(litter_size):
            b = self.__class__(names.get_first_name(), self.species)
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
    # emojis
    smile = ':cat:'
    heart = ':heart_eyes_cat:'
    sad = ':crying_cat_face:'

    def __init__(self, name, species='cat'):
        super(Cat, self).__init__(name, self.species)
        self.purr_level = random.randrange(0, 10)


class Dog(AbstractAnimal):
    """A Dog"""

    greet = "Woof"
    species = "dog"
    # emojis
    smile = ':dog:'

    def __init__(self, name, species='dog'):
        super(Dog, self).__init__(name, self.species)
        self.loyality_level = random.randrange(5, 10)


class Animal(AbstractAnimal):
    """An animal"""

    greet = "hey"
    species = ""

    def __init__(self, name, species=''):
        super(Animal, self).__init__(name, species)
        if self.species == '':
            self.species = random.choice(possible_animals.keys())
        self.smile = possible_animals[self.species]

possible_animals = {'mouse': ':mouse:',
                    'hamster': ':hamster:',
                    'rabbit': ':rabbit:',
                    'koala': ':koala:',
                    'frog': ':frog:',
                    'monkey': ':monkey:',
                    'panda': ':panda_face:',
                    'fish': ':fish:'}
