import unittest

from person import Person


class TestIsMutant(unittest.TestCase):

    def test_is_mutant_horizontal(self):
        data = ["AAAAGT",
                "GTCAGT",
                "AGTCTA",
                "GATCAG",
                "ATCGGC",
                "GTCAGC"]

        person = Person('test', '20', data)

        self.assertTrue(person.is_mutant(), 'Mutant found horizontally')

    def test_is_mutant_vertical(self):
        data = ["AGTAGT",
                "ATCAGT",
                "AGTCTA",
                "AATCAG",
                "TTCGGC",
                "GTCAGC"]

        person = Person('test', '20', data)

        self.assertTrue(person.is_mutant(), 'mutant found vertically')

    def test_is_mutant_diagonal_right(self):
        data = ["AGTAGT",
                "AACAGT",
                "GGACTA",
                "AATAAG",
                "TTCGGC",
                "GTCAGC"]

        person = Person('test', '20', data)

        self.assertTrue(person.is_mutant(), 'mutant found oblique')

    def test_is_mutant_diagonal_left(self):
        data = ["AGTAGT",
                "AGCATT",
                "GGATTA",
                "AATAAG",
                "TTCGGC",
                "GTCAGC"]

        person = Person('test', '20', data)

        self.assertTrue(person.is_mutant(), 'mutant found oblique')

    def test_is_not_mutant(self):
        data = ["AGTAGT",
                "AACAGT",
                "GGTCTA",
                "AATAAG",
                "TTCGGC",
                "GTCAGC"]

        person = Person('test', '20', data)

        self.assertFalse(person.is_mutant(), 'is not mutant')


if __name__ == '__main__':
    unittest.main()
