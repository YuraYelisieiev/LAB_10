import random
import animal


class Ecosystem:
    def __init__(self):
        self.river = [random.choice([[], [animal.Bear(
            gender=random.choice([True, False]),
            power=round(random.uniform(0.0, 1.0), 3))], [animal.Fish(
            gender=random.choice([True, False]),
            power=round(random.uniform(0.0, 1.0), 3))], [animal.Otter(
            gender=random.choice([True, False]),
            power=round(random.uniform(0.0, 1.0), 3))]]) for i
                      in range(random.randint(3, 10))]
        self.river_len = len(self.river)
        print(self.river)
        self.try_to_go()

    def move(self, anm, old_ind, operator):
        if old_ind == 0:
            operator = False
        elif old_ind == len(self.river) - 1:
            operator = True
        if operator is None:
            # stay
            return
        elif operator == 1:
            # left
            new_ind = old_ind - 1
        else:
            # right
            new_ind = old_ind + 1
        # moving an element
        self.river[old_ind].remove(anm)
        self.river[new_ind].append(anm)
        if len(self.river[new_ind]) > 1:
            # take new elements after act as return and key "new"
            ret = anm.act(self.river[new_ind][0])["new"]
            # placing new objects in father square
            self.river[new_ind] = ret
            if len(self.river[new_ind]) > 2:
                # returning object after acting on default position
                self.river[old_ind].append(ret.pop(0))
                # placing childrens
                if self.river.count([]) == 0:
                    return
                for i in range(self.river_len):
                    if not self.river[i] and len(ret) != 1:
                        self.river[i].append(self.river[new_ind].pop(1))

    def try_to_go(self):
        # animals move 1 by 1
        for i in range(100):
            for cell in self.river:
                if cell:
                    # adding age in each iter
                    # if after this iter river will be empty
                    # process will finish
                    if cell[0].check_age():
                        self.river[self.river.index(cell)] = []
                    else:
                        cell[0].age += 1
                        # True = stay
                        # False = left
                        # None = right
                        operator = random.choice([True, False, None])
                        self.move(cell[0], self.river.index(cell), operator)
                        print(self.river)


ex = Ecosystem()
