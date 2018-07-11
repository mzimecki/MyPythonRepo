import collections


class Person:

    def __init__(self, name, is_car_dealer, friends):
        self.name = name
        self.friends = friends
        self.is_car_dealer = is_car_dealer


john = Person('John', True, [])
patrice = Person('Patrice', False, [])
tamara = Person('Tamara', False, [])
jerry = Person('Jerry', False, [])
cecil = Person('Cecil', False, [tamara, jerry])
alice = Person('Alice', False, [patrice])
bart = Person('Bart', False, [john, patrice])
me = Person('Me', False, [alice, bart, cecil])


def search(person):
    search_queue = collections.deque()
    search_queue += person.friends
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person.is_car_dealer:
                print(person.name + ' is a car dealer!')
                return True
            else:
                search_queue += person.friends
                searched.append(person)
    return False


search(me)




