class ElementoDaListaSimples:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

    # __repr__ Criar uma maneira de como o objeto e mostrado fora da funcao print()
    def __repr__(self):
        return self.dado

class ListaEncadeadaSimples:
    def __init__(self, nodos=None):
        self.head = None
        if nodos is not None: # Limpa alguns itens desnecessários da lista
            nodo = ElementoDaListaSimples(dado=nodos.pop(0))
            self.head = nodo
            for elem in nodos:
                nodo.proximo = ElementoDaListaSimples(dado=elem)
                nodo = nodo.proximo

    def __repr__(self):
        nodo = self.head
        nodos = []

        while nodo is not None:
            nodos.append(nodo.dado)
            nodo = nodo.proximo

        nodos.append("None")
        return " -> ".join(nodos)

    def __iter__(self):
        nodo = self.head
        while nodo is not None:
            yield nodo
            nodo = nodo.proximo

    def inserir_no_inicio(self, nodo):
        nodo.proximo = self.head
        self.head = nodo

    def inserir_no_final(self, nodo):
        if self.head is None:
            self.head = nodo
            return

        nodo_atual = self.head
        while nodo_atual.proximo is not None:
            nodo_atual = nodo_atual.proximo

        nodo_atual.proximo = nodo
        return

    def remover(self, dado):
        if self.head is None:
            raise Exception("A lista está vazia!")

        if self.head.dado == dado:
            self.head = self.head.proximo
            return

        nodo_anterior = self.head
        for nodo in self:
            if nodo.dado == dado:
                nodo_anterior.proximo = nodo.proximo
                return
            nodo_anterior = nodo

        raise Exception("Nó com o dado '%s' não foi econtrado." % dado)

lista = ListaEncadeadaSimples()

lista.inserir_no_inicio(ElementoDaListaSimples(dado="40"))
lista.inserir_no_inicio(ElementoDaListaSimples(dado="4"))
lista.inserir_no_inicio(ElementoDaListaSimples(dado="15"))
lista.inserir_no_inicio(ElementoDaListaSimples(dado="7"))

lista.inserir_no_final(ElementoDaListaSimples(dado="12"))
lista.inserir_no_final(ElementoDaListaSimples(dado="24"))

for nodo in lista:
    print(nodo, end=' -> ')
print("None")

lista.remover(dado="40")

for nodo in lista:
    print(nodo, end=' -> ')
print("None")