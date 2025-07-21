class BST(object):
    def __init__(self, dado):
        self.dado = dado
        self.esquerda = None
        self.direita = None
        self.altura = 1

class AVL(object):

    def inserir(self, root, dado):

        # Passo 1 - BST convencional
        if not root:
            return BST(dado)
        elif dado < root.dado:
            root.esquerda = self.inserir(root.esquerda, dado)
        else:
            root.direita = self.inserir(root.direita, dado)

        # Passo 2 - Atualiza a altura do nó pai
        root.altura = 1 + max(self.get_altura(root.esquerda),
                              self.get_altura(root.direita))

        # Passo 3 - Balanceamento
        balanceamento = self.get_balanceamento(root)

        # Passo 4 - se o nó estiver desbalanceado,
        # tenta uma das rotações abaixo

        # Direita
        if balanceamento > 1 and dado < root.esquerda.dado:
            return self.direita_rotacao(root)

        # Esquerda
        if balanceamento < -1 and dado > root.direita.dado:
            return self.esquerda_rotacao(root)

        # Dupla - Esquerda Direita
        if balanceamento > 1 and dado > root.esquerda.dado:
            root.esquerda = self.esquerda_rotacao(root.esquerda)
            return self.direita_rotacao(root)

        # Dupla - Direita Esquerda
        if balanceamento < -1 and dado < root.direita.dado:
            root.direita = self.direita_rotacao(root.direita)
            return self.esquerda_rotacao(root)

        return root

    def esquerda_rotacao(self, z):

        y = z.direita
        T2 = y.esquerda

        # Rotacionando
        y.esquerda = z
        z.direita = T2

        # Atualiza os valores das alturas
        z.altura = 1 + max(self.get_altura(z.esquerda),
                           self.get_altura(z.direita))
        y.altura = 1 + max(self.get_altura(y.esquerda),
                           self.get_altura(y.direita))

        # retorna novo root
        return y

    def direita_rotacao(self, z):

        y = z.esquerda
        T3 = y.direita

        #Rotacionando
        y.direita = z
        z.esquerda = T3

        # Atualiza os valores das alturas
        z.altura = 1 + max(self.get_altura(z.esquerda),
                           self.get_altura(z.direita))
        y.altura = 1 + max(self.get_altura(y.esquerda),
                           self.get_altura(y.direita))

        # retorna novo root
        return y

    def get_altura(self, root):
        if not root:
            return 0

        return root.altura

    def get_balanceamento(self, root):
        if not root:
            return 0

        return self.get_altura(root.esquerda) - self.get_altura(root.direita)

    def em_ordem(self, root):

        if not root:
            return

        self.em_ordem(root.esquerda)
        print("{0} ".format(root.dado), end="")
        self.em_ordem(root.direita)


# Programa principal
#             30
#            /  \
#          20   40
#         /  \     \
#        10  25    50

tree = AVL()
root = None

root = tree.inserir(root, 10)
root = tree.inserir(root, 20)
root = tree.inserir(root, 30)
root = tree.inserir(root, 40)
root = tree.inserir(root, 50)
root = tree.inserir(root, 25)

tree.em_ordem(root)