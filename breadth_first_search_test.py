import breadth_first_search
from unittest import TestCase
from breadth_first_search import Person


class BreadthFirstSearchTest(TestCase):

    def test_positive_search(self):
        # having
        john = Person('John', True, [])
        patrice = Person('Patrice', False, [])
        tamara = Person('Tamara', False, [])
        jerry = Person('Jerry', False, [])
        cecil = Person('Cecil', False, [tamara, jerry])
        alice = Person('Alice', False, [patrice])
        bart = Person('Bart', False, [john, patrice])
        me = Person('Me', False, [alice, bart, cecil])

        # when
        result = breadth_first_search.search(me)

        # then
        self.assertTrue(result)

    def test_negative_search(self):
        # having
        john = Person('John', False, [])
        patrice = Person('Patrice', False, [])
        tamara = Person('Tamara', False, [])
        jerry = Person('Jerry', False, [])
        cecil = Person('Cecil', False, [tamara, jerry])
        alice = Person('Alice', False, [patrice])
        bart = Person('Bart', False, [john, patrice])
        me = Person('Me', False, [alice, bart, cecil])

        # when
        result = breadth_first_search.search(me)

        # then
        self.assertFalse(result)
