"""
Tarea 7
@author: Daniela Martínez Madrid
"""


class Group:
    group: dict

    def __init__(self, group):
        self.group = group

    def elements(self):
        """
        It return the elements in the group

        :return: list of elements
        """
        values = set([tupla[0] for tupla in self.group.keys()])
        elements = list(values)
        return elements

    def is_operation_binary(self):
        """
        It verifies that operation binary is well defined
        :parameter: g: dict
        """
        for value in self.group.values():
            if value not in self.elements():
                raise ValueError("The operation is not binary")
        return True

    def is_associativity(self):
        """
        It verifies the associativity of a group
        :parameter: g: dict that is the multiplication table
        """
        for d in self.elements():
            for b in self.elements():
                for c in self.elements():
                    if self.group[(self.group[(d, b)], c)] != self.group[(d, self.group[(b, c)])]:
                        raise ValueError("The group is not associativity")
        return True

    def identity(self):
        """
        It verifies and find the identity of a group
        :return: identity: str
        """
        i = 0
        identity = self.elements()[i]
        for element in self.elements():
            if self.group[(element, identity)] == element \
                    and self.group[(identity, element)] == element:
                continue
            if i < len(self.elements()):
                i += 1
                identity = self.elements()[i]
            else:
                print('There is no identity')
        return str(identity)

    def inverse(self, element):
        """
        It find the inverse element of a given element
        :param element: str element of a group
        :return: inverse : str its inverse element
        """
        i = 0
        inverse = self.elements()[i]
        while self.group[(element, inverse)] != self.identity():
            if i <= len(self.elements()):
                i += 1
                inverse = self.elements()[i]
            else:
                print('there is no inverse')
                return None
        return inverse

    def is_inverse(self):
        """
        It verifies if every element has inverse
        :parameter: g: dict Group multiplication table
        """
        inverses = [self.inverse(element) for element in self.elements()]
        if len([1 for e in inverses if e is None]) == 0:
            print("There is an element in group such that has not inverse ")
            return False
        else:
            print(inverses)
            return True

    def order(self, element):
        """
        It find the order of an element in a group
        :param element: str
        :return: order: int
        """
        order = 0
        aux = element
        while aux != self.identity():
            aux = self.group[(aux, '1')]
            print(aux)
            order += 1
            print(order)
        if aux == self.identity():
            print(aux)
        return str(order)

    def commutative(self):
        """
        It verifies if the group is commutative
        :parameter: g: dict
        """
        for key in g.group.keys():
            if self.group[key] == self.group[(key[1], key[0])]:
                continue
            else:
                return False
        return True


class Element(Group):

    def __init__(self, element, group):
        self.element = element
        self.group = group
        super().__init__(self.group)

    def __add__(self, other_element):
        return Element(self.group.group[(self.element, other_element.element)], self.group)

    def __sub__(self, other_element):
        return Element(self.group.group[(self.element, self.group.inverse(other_element.element))], self.group)


g = Group({('0', '0'): '0', ('0', '1'): '1', ('0', '2'): '2', ('1', '0'): '1',
           ('1', '1'): '2', ('1', '2'): '0', ('2', '0'): '2', ('2', '1'): '0', ('2', '2'): '1'})

print(g.group.keys())
print(g)
print(g.group)
a = Element('1', g)
print('El grupo del elemento a', a.group)
print('Los elementos del grupo son:', g.elements())
print(g.elements()[0])
print('La intentidad del grupo es:', g.identity())
print('El orden del elemento 0 es:', g.order('0'))
print('El orden del elemnto 1 es:', g.order('1'))
print('Verifiquemos si la operación es binaria', g.is_operation_binary())
print('Verifiquemos la propiedad asociativa', g.is_associativity())
print(type(g.identity()))
print('El inverso del elemento 2 es:', g.inverse('2'))
print(g.is_inverse())
print(g.is_operation_binary())
p1 = Element('0', g)
p2 = Element('2', g)
p3 = p1 + p2
print(p1.element)
print(p2.element)
print(p3.element)
print(type(p3))
p4 = p1.__sub__(p2)
print('p4 es', p4.element)
print(type(p4))
