import collections


class Person:

    def __init__(self, name, is_car_dealer, friends):
        self.name = name
        self.friends = friends
        self.is_car_dealer = is_car_dealer


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
