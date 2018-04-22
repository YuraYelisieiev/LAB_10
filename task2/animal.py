import random


class Animal:
    def __init__(self, power=1, gender=False):
        self.power = power
        self.gender = gender

    def check_power(self, other):
        if self.power > other.power:
            return [self]
        elif self.power < other.power:
            return [other]
        else:
            # if powers are equal then they will die in a fight
            return []

    def kids(self, other):
        self.kids(other)

    def act(self, other):
        if type(self) == type(other):
            if self.gender == other.gender:
                return {"old": [self, other], "new": self.check_power(other)}
            else:
                return {"old": [self, other],
                        "new": self.kids(other)["new"]}


class Fish(Animal):
    All = []

    def __init__(self):
        super().__init__(gender=random.choice([True, False]),
                         power=round(random.uniform(0.0, 1.0), 3))
        Fish.All.append(self)

    def act(self, other):
        check = super().act(other)
        if check:
            return check
        return {"old": [self, other], "new": [other]}

    def kids(self, other):
        kids = [self, other]
        kids += [self.__class__()]
        return {"old": [self, other], "new": kids}

    def __repr__(self):
        return "Fish({}, {})".format(self.power, self.gender)


class Bear(Animal):
    All = []

    def __init__(self):
        super().__init__(gender=random.choice([True, False]),
                         power=round(random.uniform(0.0, 1.0), 3))
        Bear.All.append(self)

    def act(self, other):
        check = super().act(other)
        if check:
            return check
        return {"old": [self, other], "new": [self]}

    def kids(self, other):
        kids = [self, other]
        kids += [self.__class__()]
        return {"old": [self, other], "new": kids}

    def __repr__(self):
        return "Bear({}, {})".format(self.power, self.gender)
