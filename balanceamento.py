import unittest


class Pilha():
    def __init__(self):
        self._lista = []

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

def bora(cont, teste, pilha):

    n = teste[cont]
    if n in '{[(':
        pilha.empilhar(n)
                
    if n in '}])':
        if n == '}' and pilha.desempilhar() != '{':
            return False
                
        if n == ']' and pilha.desempilhar() != '[':
            return False
                
        if n == ')' and pilha.desempilhar() != '(':
            return False 
    
    cont = cont + 1
    if len(teste) == cont:
        if pilha.vazia():
            return True
        return False    
    return bora(cont, teste, pilha)

def esta_balanceada(teste):
    """
    Função que calcula se expressão possui parenteses, colchetes e chaves balanceados
    O Aluno deverá informar a complexidade de tempo e espaço da função
    Deverá ser usada como estrutura de dados apenas a pilha feita na aula anterior
    :param expressao: string com expressao a ser balanceada
    :return: boleano verdadeiro se expressao está balanceada e falso caso contrário
    """
    pass
    if teste:

        pilha = Pilha()
        cont = 0
        if teste[0] in '}])':
            return False
        return bora(cont, teste, pilha)
        
    else:
        return True
            

class BalancearTestes(unittest.TestCase):
    def test_expressao_vazia(self):
        self.assertTrue(esta_balanceada(''))

    def test_parenteses(self):
        self.assertTrue(esta_balanceada('()'))

    def test_chaves(self):
        self.assertTrue(esta_balanceada('{}'))

    def test_colchetes(self):
        self.assertTrue(esta_balanceada('[]'))

    def test_todos_caracteres(self):
        self.assertTrue(esta_balanceada('({[]})'))
        self.assertTrue(esta_balanceada('[({})]'))
        self.assertTrue(esta_balanceada('{[()]}'))

    def test_chave_nao_fechada(self):
        self.assertFalse(esta_balanceada('{'))

    def test_colchete_nao_fechado(self):
        self.assertFalse(esta_balanceada('['))

    def test_parentese_nao_fechado(self):
        self.assertFalse(esta_balanceada('('))

    def test_chave_nao_aberta(self):
        self.assertFalse(esta_balanceada('}{'))

    def test_colchete_nao_aberto(self):
        self.assertFalse(esta_balanceada(']['))

    def test_parentese_nao_aberto(self):
        self.assertFalse(esta_balanceada(')('))

    def test_falta_de_caracter_de_fechamento(self):
        self.assertFalse(esta_balanceada('({[]}'))

    def test_falta_de_caracter_de_abertura(self):
        self.assertFalse(esta_balanceada('({]})'))

    def test_expressao_matematica_valida(self):
        self.assertTrue(esta_balanceada('({[1+3]*5}/7)+9'))

    def test_char_errado_fechando(self):
        self.assertFalse(esta_balanceada('[)'))
        
        

if __name__ == '__main__':
    unittest.main()
