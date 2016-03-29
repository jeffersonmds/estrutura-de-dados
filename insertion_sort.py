import unittest

def insertion_sort(seq):
    for k in range(1, len(seq)):
        n1=k
        n2=n1-1 
        while n1>=1 and seq[n1]<seq[n2]:
            cont=seq[n1]
            seq[n1]= seq[n2]
            seq[n2]= cont
            n1=n1-1
            n2=n2-1            
    return seq

class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], insertion_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], insertion_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], insertion_sort([2, 1]))

    def teste_lista_desordenada(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], insertion_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()
