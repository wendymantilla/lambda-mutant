def search_sequence_horizontal(matriz, n=4):
    for fila in matriz:
        range_fila = range(len(fila) - n + 1)  # range(0,2)
        for i in range_fila:
            f = fila[i:i + n]  # substring
            g = [fila[i]] * n  # letter multiply by 4
            if f == ''.join(g):
                print(f'horizontal found: {g}')
                return True
    return False


def search_sequence_vertical(matriz, n=4):
    filas = len(matriz)
    columnas = len(matriz[0])
    for col in range(columnas):
        ranges_col = range(filas - n + 1)
        for fila in ranges_col:
            g = matriz[fila][col]
            if all(matriz[fila + k][col] == g for k in range(n)):
                print(f'vertical found: {g}')
                return True
    return False


def search_sequence_oblicue(matriz, n=4):
    filas = len(matriz)
    columnas = len(matriz[0])

    # Buscar en diagonal hacia abajo y derecha
    for fila in range(filas - n + 1):
        for col in range(columnas - n + 1):
            g = matriz[fila][col]
            if all(matriz[fila + k][col + k] == g for k in range(n)):
                print(f'backslash found: {g}')
                return True

    # Buscar en diagonal hacia abajo y izquierda
    for fila in range(filas - n + 1):
        for col in range(n - 1, columnas):
            g = matriz[fila][col]
            if all(matriz[fila + k][col - k] == g for k in range(n)):
                print(f'slash found: {g}')
                return True

    return False


def search_sequence(matrix, n=4):
    if search_sequence_horizontal(matrix, n) or search_sequence_vertical(matrix, n) or search_sequence_oblicue(
            matrix, n):
        return True
    return False


class DNASequenceAnalyzer:
    def __init__(self, dna: list):
        self.dna = dna
        self.n = len(self.dna)

    def is_mutant(self):
        return search_sequence(self.dna, 4)
