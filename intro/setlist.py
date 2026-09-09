class SetList():
    def __init__(self):
        self._elements = []
    
    def insert(self, elem):
        self._elements.append(elem)

    def contains(self, elem):
        for element in self._elements:
            if element == elem:
                return True

        return False

    def __add__(self, elem):
        self.insert(elem)


if __name__=='__main__':
    my_set_1 = set()
    my_set_2 = SetList()

    my_set_2.insert(10)
    my_set_2.insert(20)
    my_set_2 + 15

    if my_set_2.contains(10):
        print('It contains 10!!')

    if my_set_2.contains(15):
        print('Uh oh')