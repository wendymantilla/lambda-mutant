from mutant_detector import MutantDetector

detector = MutantDetector()


class Person:
    def __init__(self, name, age, dna: list):
        self.name = name
        self.age = age
        self.dna = dna

    def is_mutant(self):
        return detector.is_mutant(self.dna)
