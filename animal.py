class Animal:
    def __init__(self, power=1, gender=False):
        self.power = power
        self.gender = gender
        self.__age = 0

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    def check_power(self, other):
        if self.power > other.power:
            return [self]
        elif self.power < other.power:
            return [other]
        else:
            # if the powers are equal to each other we are comparing age`s
            if self.__age > other.age:
                return [other]
            elif self.__age < other.age:
                return [self]
            # if ages are equal then they will die in a fight
            else:
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
    AGE = 5

    def act(self, other):
        check = super().act(other)
        if check:
            return check
        return {"old": [self, other], "new": [other]}

    def kids(self, other):
        kids = [self, other]
        kids += [self.__class__()] * 7
        return {"old": [self, other], "new": kids}

    def __repr__(self):
        return "Fish({}, {}, {})".format(self.power, self.gender, self.age)

    def check_age(self):
        if self.age == self.AGE:
            return True
        else:
            return False


class Bear(Animal):
    AGE = 10

    def act(self, other):
        check = super().act(other)
        if check:
            return check
        return {"old": [self, other], "new": [self]}

    def kids(self, other):
        kids = [self, other]
        kids += [self.__class__()] * 2
        return {"old": [self, other], "new": kids}

    def __repr__(self):
        return "Bear({}, {}, {})".format(self.power, self.gender, self.age)

    def check_age(self):
        if self.age == self.AGE:
            return True
        else:
            return False


class Otter(Animal):
    AGE = 12

    def act(self, other):
        check = super().act(other)
        if check:
            return check
        if isinstance(other, Fish):
            # eating the fish
            return {"old": [self, other], "new": [self]}
        else:
            # act with bear Runnnn :=)
            return {"old": [self, other], "new": [other]}

    def kids(self, other):
        kids = [self, other]
        kids += [self.__class__()] * 3
        return {"old": [self, other], "new": kids}

    def check_age(self):
        if self.age == self.AGE:
            return True
        else:
            return False

    def __repr__(self):
        return "Otter({}, {}, {})".format(self.power, self.gender,
                                          self.age)