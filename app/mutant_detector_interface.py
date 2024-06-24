from abc import ABC, abstractmethod


class MutantDetectorInterface(ABC):
    @abstractmethod
    def is_mutant(self, dna: list) -> bool:
        pass
