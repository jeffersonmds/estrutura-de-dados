# A função min_max deverá rodar em O(n) e o código não pode usar nenhuma
# lib do Python (sort, min, max e etc)
# Não pode usar qualquer laço (while, for), a função deve ser recursiva
# Ou delegar a solução para uma função puramente recursiva
import unittest

def bora(cont, seq, min, max):
    if cont < len(seq):
        if int(seq[cont]) > int(seq[cont + 1]) and int(seq[cont]) > max:
            max = int(seq[cont])
        if int(seq[cont]) < int(seq[cont + 1]) and int(seq[cont]) < min:
            min = int(seq[cont])
    cont = cont + 1
    if cont == (len(seq) - 1):
        if int(seq[len(seq) - 1]) > max:
            max = int(seq[len(seq) - 1])
        if int(seq[len(seq) - 1]) < min:
            min = int(seq[len(seq) - 1])
        return (min, max)

    return bora(cont, seq, min, max)

def min_max(seq):
    '''
    :param seq: uma sequencia
    :return: (min, max)
    Retorna tupla cujo primeiro valor mínimo (min) é o valor
    mínimo da sequencia seq.
    O segundo é o valor máximo (max) da sequencia

    O(n)
    '''
    if len(seq) == 0:
        return (None, None)
    if len(seq) == 1:
        return seq[0], seq[0]

    val = bora(0, seq, seq[0], seq[0])
    return val


class MinMaxTestes(unittest.TestCase):
    def test_lista_vazia(self):
        self.assertTupleEqual((None, None), min_max([]))

    def test_lista_len_1(self):
        self.assertTupleEqual((1, 1), min_max([1]))

    def test_lista_consecutivos(self):
        self.assertTupleEqual((0, 500), min_max(list(range(501))))

if __name__ == '__main__':
    unittest.main()
