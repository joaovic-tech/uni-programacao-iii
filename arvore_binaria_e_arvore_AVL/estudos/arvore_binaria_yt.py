class Folha:
    def __init__(self, valor: int):
        self.valor = valor

    def get_valor(self) -> int:
        return self.valor

class Arvore:
    def __init__(self):
        self.folha = None
        self.esquerda = None
        self.direita = None

    def is_empty(self) -> bool:
        return self.folha is None

    def inserir(self, novo: Folha):
        if self.is_empty():
            self.folha = novo
        else:
            # Inserir à esquerda
            if novo.get_valor() < self.folha.get_valor():
                if self.esquerda is None:
                    self.esquerda = Arvore()
                    print(f'Folha: {novo.get_valor()} a esquerda de {self.folha.get_valor()}')
                self.esquerda.inserir(novo)
            # Inserir à direita
            elif novo.get_valor() > self.folha.get_valor():
                if self.direita is None:
                    self.direita = Arvore()
                    print(f'Folha: {novo.get_valor()} a direita de {self.folha.get_valor()}')
                self.direita.inserir(novo)

    def inserir_invertido(self, novo: Folha):
        if self.is_empty():
            self.folha = novo
        else:
            if novo.get_valor() < self.folha.get_valor():
                if self.direita is None:
                    self.direita = Arvore()
                    print(f'Folha: {novo.get_valor()} a direita de {self.folha.get_valor()}')
                self.direita.inserir_invertido(novo)
            elif novo.get_valor() > self.folha.get_valor():
                if self.esquerda is None:
                    self.esquerda = Arvore()
                    print(f'Folha: {novo.get_valor()} a esquerda de {self.folha.get_valor()}')
                self.esquerda.inserir_invertido(novo)

    def em_ordem(self, lista: list) -> list:
        if self.esquerda:
            self.esquerda.em_ordem(lista)
        if self.folha:
            lista.append(self.folha.get_valor())
        if self.direita:
            self.direita.em_ordem(lista)
        return lista


arvore_normal = Arvore()
arvore_invertida = Arvore()

# Crie/Teste a Arvore binária abaixo
#         ( 30 )
#         /    \
#      ( 15 )  ( 45 )
#      /    \
#   ( 7 )  ( 19 )

while True:
    print('1 - Inserir na árvore binária')
    print('2 - Inserir na árvore binária invertida')
    print('3 - Remover da árvore binária')
    print('4 - Imprimir a árvore binária')
    print('5 - Limpar a árvore binária')
    print('6 - Inserir valores automáticos nas arvores (30, 15, 45, 7, 19):')
    print('7 - Sair')

    op = int(input('Escolha uma opção: '))
    if op == 1:
        valores = input('Digite cada valor a ser inserido separados por vírgula (ex: 30, 15, 45, 7, 19): ')
        valores = [int(v) for v in str(valores).split(',')]

        for valor in valores:
            arvore_normal.inserir(Folha(valor))

    elif op == 2:
        valores = input('Digite cada valor a ser inserido separados por vírgula (ex: 30, 15, 45, 7, 19): ')
        valores = [int(v) for v in str(valores).split(',')]

        for valor in valores:
            arvore_invertida.inserir(Folha(valor))
    elif op == 3:
        print('Remover da árvore binária não implementado.')
    elif op == 4:
        lista_normal = arvore_normal.em_ordem([])
        lista_invertida = arvore_invertida.em_ordem([])

        print("\n--- Impressão ---")
        if not lista_normal:
            print("Árvore Normal está vazia.")
        else:
            # Resultado deve ser ORDEM CRESCENTE
            print('Árvore Normal (em ordem):', lista_normal)

        if not lista_invertida:
            print("Árvore Invertida está vazia.")
        else:
            # Resultado deve ser ORDEM DECRESCENTE
            print('Árvore Invertida (em ordem):', lista_invertida)
        print("-----------------")

    elif op == 5:
        arvore_normal = Arvore()
        arvore_invertida = Arvore()
        print('Ambas as árvores foram limpas.')
    elif op == 6:
        valores = [30, 15, 45, 7, 19]
        print(f"Inserindo valores de teste: {valores}")

        for valor in valores:
            arvore_normal.inserir(Folha(valor))

        print('-' * 20)

        for valor in valores:
            arvore_invertida.inserir_invertido(Folha(valor))

        print("Valores de teste inseridos em ambas as árvores.")
    elif op == 7:
        break
    else:
        print('Opção inválida. Tente novamente.')