class Group:
    group: dict

    def __init__(self, group):
        self.group = group

    def elements(self):
        values = set([value for value in self.group.values()])
        elements = list(values)
        return elements

    def identity(self):
        i = 0
        identity = self.elements()[i]
        for element in self.elements():
            if self.group[(element, identity)] == element \
                    and self.group[(identity, element)] == element:
                pass
            elif i < len(self.elements()):
                i += 1
                identity = self.elements()[i]
            else:
                print('There is no identity')
        return str(identity)

    def order(self, element):
        order = 0
        aux = element
        while aux != self.identity():
            aux = self.group[(aux, '1')]
            print(aux)
            order += 1
            print(order)
        if aux == self.identity():
            print('para por favor')
        return str(order)

    def commutative(self):
        for key in g.group.keys():
            if self.group[key] == self.group[(key[1], key[0])]:
                pass
            else:
                return False
        return True


class Element(Group):

    def __init__(self, element, group):
        self.element = element
        self.group = group
        super().__init__(self.group)

    def __add__(self, other_element):
        return Element(self.group[(self.element, other_element.element)], self.group)


g = Group({('0', '0'): '0', ('0', '1'): '1', ('0', '2'): '2', ('1', '0'): '1',
           ('1', '1'): '2', ('1', '2'): '0', ('2', '0'): '2', ('2', '1'): '0', ('2', '2'): '1'})

print(g.group.keys())
print(g)
print(g.group)
a = Element('1', g)
print('El grupo del elemento a', a.group)
print(g.elements())
print(g.elements()[0])
print(g.identity())
print(g.order('0'))
print(g.order('1'))
print(type(g.identity()))
