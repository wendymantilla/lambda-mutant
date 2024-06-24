from mutant_detector_interface import MutantDetectorInterface
from dna_sequence_analyzer import DNASequenceAnalyzer


class MutantDetector(MutantDetectorInterface):

    def is_mutant(self, dna: list) -> bool:
        analyzer = DNASequenceAnalyzer(dna)
        return analyzer.is_mutant()
