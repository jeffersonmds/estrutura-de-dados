class Noh:
    def __init__(self, valor, pai=None):
        self.filhos=[]
        self.valor=valor
        self.pai=pai
        self.filho_esquerdo=None
        self.irmao_direito=None
        if pai:
            pai.filho_esquerdo=self        

    def adicionar(self, filho):
        filho.pai=self
        if len(self.filhos)>0:
            fil=self.filho_esquerdo
            while fil.irmao_direito:
                fil=fil.irmao_direito
            fil.irmao_direito=filho
        else:
            self.filho_esquerdo=filho
        self.filhos.append(filho)

class Arvore:
    def __init__(self, raiz=None):
        self.raiz=raiz

    def altura(self):
        h=0
        aux=self.raiz
        while aux:
            aux=aux.filho_esquerdo
            h=h+1
        return h

    def __iter__(self):
        if self.raiz==None:
            return self.raiz
        pilha=[]
        
        pilha.append(self.raiz)
        while pilha:
            tet = pilha.pop()
            if tet.irmao_direito:
                pilha.append(tet.irmao_direito)
            if tet.filho_esquerdo:
                pilha.append(tet.filho_esquerdo)
            yield tet.valor



from unittest.case import TestCase


class NohTestes(TestCase):
    def teste_init_com_defaults(self):
        noh = Noh(5)
        self.assertEqual(5, noh.valor)
        self.assertIsNone(noh.pai)
        self.assertIsNone(noh.irmao_direito)
        self.assertIsNone(noh.filho_esquerdo)

    def teste_init_com_pai_justaposto(self):
        pai = Noh(5)
        filho = Noh(4, pai)
        self.assertIs(pai, filho.pai)
        self.assertIs(filho, pai.filho_esquerdo)

    def teste_init_com_pai_nomeado(self):
        pai = Noh(5)
        filho = Noh(4, pai=pai)
        self.assertIs(pai, filho.pai)
        self.assertIs(filho, pai.filho_esquerdo)

    def teste_adicionar_um_filho(self):
        pai = Noh(5)
        filho = Noh(4)
        pai.adicionar(filho)
        self.assertIs(pai, filho.pai)
        self.assertIs(filho, pai.filho_esquerdo)
        self.assertIsNone(filho.irmao_direito)

    def teste_adicionar_dois_filhos(self):
        pai = Noh(5)
        filho = Noh(4)
        filho2 = Noh(3)
        pai.adicionar(filho)
        pai.adicionar(filho2)
        self.assertIs(pai, filho.pai)
        self.assertIs(filho, pai.filho_esquerdo)
        self.assertIs(filho2, filho.irmao_direito)
        self.assertIsNone(filho2.irmao_direito)

    def teste_adicionar_tres_filhos(self):
        pai = Noh(5)
        filho = Noh(4)
        filho2 = Noh(3)
        filho3 = Noh(2)
        pai.adicionar(filho)
        pai.adicionar(filho2)
        pai.adicionar(filho3)
        self.assertIs(pai, filho.pai)
        self.assertIs(filho, pai.filho_esquerdo)
        self.assertIs(filho2, filho.irmao_direito)
        self.assertIs(filho3, filho2.irmao_direito)
        self.assertIsNone(filho3.irmao_direito)


class ArvoreTestes(TestCase):
    def teste_init(self):
        arvore = Arvore()
        self.assertIsNone(arvore.raiz)

    def teste_arvore_com_raiz(self):
        noh = Noh(1)
        arvore = Arvore(noh)
        self.assertIs(noh, arvore.raiz)

    def teste_altura_arvore(self):
        self.assertEqual(0, Arvore().altura())
        self.assertEqual(1, Arvore(Noh(1)).altura())
        arvore_binaria = self.gerar_arvore_binaria()
        self.assertEqual(4, arvore_binaria.altura())

    def test_travesia_em_profundidade(self):
        travessia_arvore_vazia = [i for i in Arvore()]
        self.assertListEqual([], travessia_arvore_vazia)
        travessia_arvore_unitaria = [i for i in Arvore(Noh(1))]
        self.assertListEqual([1], travessia_arvore_unitaria)
        arvore_binaria = self.gerar_arvore_binaria()
        travessia_arvore_binaria = [i for i in arvore_binaria]
        pos_ordem = [0, 1, 3, 4, 2, 6, 7, 9, 8, 5]
        pre_ordem = [5, 2, 1, 0, 4, 3, 8, 7, 6, 9]
        self.assertTrue(travessia_arvore_binaria == pos_ordem or travessia_arvore_binaria == pre_ordem)

    def gerar_arvore_binaria(self):
        nohs = [Noh(i) for i in range(10)]
        raiz = nohs[5]
        raiz.adicionar(nohs[2])
        raiz.adicionar(nohs[8])

        nohs[2].adicionar(nohs[1])
        nohs[2].adicionar(nohs[4])

        nohs[1].adicionar(nohs[0])

        nohs[4].adicionar(nohs[3])

        nohs[8].adicionar(nohs[7])
        nohs[8].adicionar(nohs[9])

        nohs[7].adicionar(nohs[6])

        return Arvore(raiz)

import unittest

if __name__ == '__main__':
    unittest.main()
