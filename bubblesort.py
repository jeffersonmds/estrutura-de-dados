def bubble_sort(seq):
    '''
    Tempo: O(n^2)
    Memoria: O(1)
    '''
    tam = len(seq)-1
    for cont in range(tam):
        if seq == sorted(seq):
            return seq
        for cont2 in range(tam):
            if seq[cont2]>seq[cont2+1]: seq[cont2], seq[cont2+1]=seq[cont2+1], seq[cont2]
    return seq

import unittest
class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], bubble_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], bubble_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], bubble_sort([1, 2]))

    def teste_lista_binaria(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], bubble_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()
