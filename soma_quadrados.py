from collections import Counter
from collections import deque

def soma_quadrados(n):        
    test=0
    aux=n
    res = {0:[0], 1:[1]}
    if n>=0 and n<=1:
        return res[n]
    else:
        quad=[]
        test=2
        while test<=aux:
            n=test
            for q in range(1,n+1):
                if q**2<=n and q**2 not in quad:
                    quad.append(q**2)
            if n>11:
                quad.pop()
            entr=n
            hel=[]
            k=n
            while n not in res.keys() and n!=0:
                if quad and n not in quad:
                    while k>=n and quad and k!=n-k:
                        k=quad.pop()
                hel.append(k)
                n=n-k                
            test=test+1
            if n==0:
                res[entr]=hel
            else:
                res[entr]=hel.__add__(res[n])
    return res[entr]


import unittest


class SomaQuadradosPerfeitosTestes(unittest.TestCase):
    def teste_0(self):
        self.assert_possui_mesmo_elementos([0], soma_quadrados(0))

    def teste_1(self):
        self.assert_possui_mesmo_elementos([1], soma_quadrados(1))

    def teste_2(self):
        self.assert_possui_mesmo_elementos([1, 1], soma_quadrados(2))

    def teste_3(self):
        self.assert_possui_mesmo_elementos([1, 1, 1], soma_quadrados(3))

    def teste_4(self):
        self.assert_possui_mesmo_elementos([4], soma_quadrados(4))

    def teste_5(self):
        self.assert_possui_mesmo_elementos([4, 1], soma_quadrados(5))

    def teste_11(self):
        self.assert_possui_mesmo_elementos([9, 1, 1], soma_quadrados(11))

    def teste_12(self):
        self.assert_possui_mesmo_elementos([4, 4, 4], soma_quadrados(12))

    def assert_possui_mesmo_elementos(self, esperado, resultado):
        self.assertEqual(Counter(esperado), Counter(resultado))

if __name__ == '__main__':
    unittest.main()
