# Exercício de avaliação de expressão aritmética.
# Só podem ser usadas as estruturas Pilha e Fila implementadas em aulas anteriores.
# Deve ter análise de tempo e espaço para função avaliação

#OBS: Tive uma série de problemas com o import no idle, por isso recorri a copiar os código de pilha e fila já feitos anteriormente

class Pilha():
    def __init__(self):
        self._lista = []
        
    def __len__(self):
        return len(self._lista)
    
    def vazia(self):
        return not bool(self._lista)

    def topo(self):
        if self._lista:
            return self._lista[-1]

        raise PilhaVaziaErro()

    def empilhar(self, valor):
        self._lista.append(valor)

    def desempilhar(self):
        try:
            return self._lista.pop()
        except IndexError:
            raise PilhaVaziaErro()


class PilhaVaziaErro(Exception):
    pass

from collections import deque

class Fila():
    def __init__(self):
        self._deque = deque()

    def __len__(self):
        return len(self._deque)

    def __iter__(self):
        try:
            while True:
                yield self.desenfileirar()
        except FilaVaziaErro:
            pass

    def enfileirar(self, val):
        return self._deque.append(val)

    def vazia(self):
        return len(self) == 0

    def primeiro(self):
        try:
            return self._deque[0]
        except IndexError:
            raise FilaVaziaErro

    def desenfileirar(self):
        try:
            return self._deque.popleft()
        except IndexError:
            raise FilaVaziaErro


class FilaVaziaErro(Exception):
    pass

class ErroLexico(Exception):
    pass


class ErroSintatico(Exception):
    pass

#------------------------------------------------------

def analise_lexica(expressao):
    """
    Executa análise lexica transformando a expressao em fila de objetos:
    Transforma inteiros em ints
    Flutuantes em floats
    e verificar se demais caracteres são validos: +-*/(){}[]
    :param expressao: string com expressao a ser analisada
    :return: fila com tokens
    """
    fila = Fila()
    vra = R"0123456789.-+*/{}[]()"

    if expressao:
        test = ''
        for i in expressao:
            if i in vra:
                if i in '{}.[]-+*/()':
                    if test:
                        fila.enfileirar(test)
                        test = ''
                    fila.enfileirar(i)
                else:
                    test=test+i
            else:
                raise ErroLexico()
        if test:
            fila.enfileirar(test)
    return fila

def analise_sintatica(fila):
    """
    Função que realiza analise sintática de tokens produzidos por analise léxica.
    Executa validações sintáticas e se não houver erro retorn fila_sintatica para avaliacao
    :param fila: fila proveniente de análise lexica
    :return: fila_sintatica com elementos tokens de numeros
    """
    if fila.__len__():
        fila_sintetica = Fila()
        test = ''
        for i in range(fila.__len__()):
            if fila._deque[i] in '-+/*(){}[]':
                if test:
                    if '.' in test:
                        fila_sintetica.enfileirar(float(test))
                    else:
                        fila_sintetica.enfileirar(int(test))
                test = ''
                fila_sintetica.enfileirar(fila._deque[i])
            else:
                test = test + fila._deque[i]

        if test:
            if '.' in test:
                fila_sintetica.enfileirar(float(test))
            else:
                fila_sintetica.enfileirar(int(test))

        return fila_sintetica
    else:
        raise ErroSintatico


def avaliar(expressao):
    """
    Função que avalia expressão aritmetica retornando se val se não houver nenhum erro
    :param expressao: string com expressão aritmética
    :return: val númerico com resultado
    tempo e memoria: O(n)
    """

    if expressao:

        fila = analise_sintatica(analise_lexica(expressao))
        if fila.__len__()==1:
            return fila.primeiro()
        else:
            pilha=Pilha()

            for i in range(fila.__len__()):
                pilha.empilhar(fila._deque[i])
                if pilha.__len__()>=3 and str(pilha.topo()) not in '-+*/(){}[]':
                    val=pilha.topo()
                    pilha.desempilhar()

                    if pilha.topo()=='+':
                        pilha.desempilhar()
                        val = pilha.desempilhar() + val
                    elif pilha.topo()=='-':
                        pilha.desempilhar()
                        val = pilha.desempilhar() - val
                    elif pilha.topo()=='*':
                        pilha.desempilhar()
                        val = pilha.desempilhar() * val
                    elif pilha.topo()=='/':
                        pilha.desempilhar()
                        val = pilha.desempilhar() / val
                    pilha.empilhar(val)
                    val = ''
                elif str(pilha.topo()) in ')}]' and i == fila.__len__() - 1:
                    pilha.desempilhar()
                    
                    while len(pilha)>1:
                        if str(pilha.topo()) not in '-+*/(){}[]':
                            val = pilha.topo()
                            pilha.desempilhar()

                            if pilha.topo()=='+':
                                pilha.desempilhar()
                                val = pilha.desempilhar() + val
                            elif pilha.topo()=='-':
                                pilha.desempilhar()
                                val = pilha.desempilhar() - val
                            elif pilha.topo()=='*':
                                pilha.desempilhar()
                                val = pilha.desempilhar() * val
                            elif pilha.topo()=='/':
                                pilha.desempilhar()
                                val = pilha.desempilhar() / val
                            elif str(pilha.topo()) in '(){}[]':
                                pilha.desempilhar()
                            pilha.empilhar(val)
                            val = ''
                        else:
                            pilha.desempilhar()
            return pilha.topo()
    raise ErroSintatico()


import unittest


class AnaliseLexicaTestes(unittest.TestCase):
    def test_expressao_vazia(self):
        fila = analise_lexica('')
        self.assertTrue(fila.vazia())

    def test_caracter_estranho(self):
        self.assertRaises(ErroLexico, analise_lexica, 'a')
        self.assertRaises(ErroLexico, analise_lexica, 'ab')

    def test_inteiro_com_um_algarismo(self):
        fila = analise_lexica('1')
        self.assertEqual('1', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_inteiro_com_vários_algarismos(self):
        fila = analise_lexica('1234567890')
        self.assertEqual('1234567890', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_float(self):
        fila = analise_lexica('1234567890.34')
        self.assertEqual('1234567890', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('34', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_parenteses(self):
        fila = analise_lexica('(1)')
        self.assertEqual('(', fila.desenfileirar())
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual(')', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_chaves(self):
        fila = analise_lexica('{(1)}')
        self.assertEqual('{', fila.desenfileirar())
        self.assertEqual('(', fila.desenfileirar())
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual(')', fila.desenfileirar())
        self.assertEqual('}', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_colchetes(self):
        fila = analise_lexica('[{(1.0)}]')
        self.assertEqual('[', fila.desenfileirar())
        self.assertEqual('{', fila.desenfileirar())
        self.assertEqual('(', fila.desenfileirar())
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertEqual(')', fila.desenfileirar())
        self.assertEqual('}', fila.desenfileirar())
        self.assertEqual(']', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_adicao(self):
        fila = analise_lexica('1+2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('+', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_subtracao(self):
        fila = analise_lexica('1-2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('-', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_multiplicacao(self):
        fila = analise_lexica('1*2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('*', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_divisao(self):
        fila = analise_lexica('1/2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('/', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_expresao_com_todos_simbolos(self):
        expressao = '1/{2.0+3*[7-(5-3)]}'
        fila = analise_lexica(expressao)
        self.assertListEqual(list(expressao), [e for e in fila])
        self.assertTrue(fila.vazia())


class AnaliseSintaticaTestes(unittest.TestCase):
    def test_fila_vazia(self):
        fila = Fila()
        self.assertRaises(ErroSintatico, analise_sintatica, fila)

    def test_int(self):
        fila = Fila()
        fila.enfileirar('1234567890')
        fila_sintatica = analise_sintatica(fila)
        self.assertEqual(1234567890, fila_sintatica.desenfileirar())
        self.assertTrue(fila_sintatica.vazia())

    def test_float(self):
        fila = Fila()
        fila.enfileirar('1234567890')
        fila.enfileirar('.')
        fila.enfileirar('4')
        fila_sintatica = analise_sintatica(fila)
        self.assertEqual(1234567890.4, fila_sintatica.desenfileirar())
        self.assertTrue(fila_sintatica.vazia())

    def test_expressao_com_todos_elementos(self):
        fila = analise_lexica('1000/{222.125+3*[7-(5-3)]}')
        fila_sintatica = analise_sintatica(fila)
        self.assertListEqual([1000, '/', '{', 222.125, '+', 3, '*', '[', 7, '-', '(', 5, '-', 3, ')', ']', '}'],[e for e in fila_sintatica])


class AvaliacaoTestes(unittest.TestCase):
    def test_expressao_vazia(self):
        self.assertRaises(ErroSintatico, avaliar, '')

    def test_inteiro(self):
        self.assert_avaliacao('1')

    def test_float(self):
        self.assert_avaliacao('2.1')

    def test_soma(self):
        self.assert_avaliacao('2+1')

    def test_subtracao_e_parenteses(self):
        self.assert_avaliacao('(2-1)')

    def test_expressao_com_todos_elementos(self):
        self.assertEqual(1.0, avaliar('2.0/[4*3+1-{15-(1+3)}]'))

    def assert_avaliacao(self, expressao):
        self.assertEqual(eval(expressao), avaliar(expressao))


if __name__ == '__main__':
    unittest.main()
