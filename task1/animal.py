class Animal:
    def kids(self, other):
        self.kids(other)

    def act(self, other):
        if type(self) == type(other):
            return {"old": [self, other], "new": self.kids(other)["new"]}


class Fish(Animal):
    All = []

    def __init__(self):
        super().__init__()
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
        return "Fish"


class Bear(Animal):
    All = []

    def __init__(self):
        super().__init__()
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
        return "Bear"
