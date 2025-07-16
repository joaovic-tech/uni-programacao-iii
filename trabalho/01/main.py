class Nodo:
  def __init__(self, numero, cor):
    self.numero = numero
    self.cor = cor
    self.proximo = None


class Clinica:
  def __init__(self):
    self.head = None
    self.contadorV = 1
    self.contadorA = 201

  def inserirSemPrioridade(self, nodo):
    if not self.head:
      self.head = nodo
      return
    atual = self.head
    while atual.proximo:
      atual = atual.proximo
    atual.proximo = nodo

  def inserirComPrioridade(self, nodo):
    if not self.head or self.head.cor == "V":
      nodo.proximo = self.head
      self.head = nodo
      return
    atual = self.head
    while atual.proximo and atual.proximo.cor == "A":
      atual = atual.proximo
    nodo.proximo = atual.proximo
    atual.proximo = nodo

  def inserir(self):
    while True:
      cor = input("Informe a cor do cartão (A/V): ").strip().upper()
      if cor in ("A", "V"):
        break
      print("Cor inválida. Tente novamente.")

    if cor == "V":
      numero = self.contadorV
      self.contadorV += 1
    else:
      numero = self.contadorA
      self.contadorA += 1

    nodo = Nodo(numero, cor)

    if not self.head:
      self.head = nodo
    elif cor == "V":
      self.inserirSemPrioridade(nodo)
    else:
      self.inserirComPrioridade(nodo)

  def imprimirListaEspera(self):
    if not self.head:
      print("Fila vazia.")
      return
    atual = self.head
    print("Lista de espera:")
    while atual:
      print(f"Cartão {atual.cor} - Número {atual.numero}")
      atual = atual.proximo

  def atenderPaciente(self):
    if not self.head:
      print("Nenhum paciente na fila.")
      return
    nodo = self.head
    self.head = self.head.proximo
    print(f"Atendendo o paciente cartão cor {nodo.cor} e número {nodo.numero}.")


def menu():
  lista = Clinica()
  while True:
    print("\n1 - Adicionar paciente a fila")
    print("2 - Mostrar pacientes na fila")
    print("3 - Chamar paciente")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ").strip()
    if opcao == "1":
      lista.inserir()
    elif opcao == "2":
      lista.imprimirListaEspera()
    elif opcao == "3":
      lista.atenderPaciente()
    elif opcao == "4":
      print("Encerrando o programa.")
      break
    else:
      print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
  menu()
