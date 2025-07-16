class EmplacamentoPorEstado:
  def __init__(self, sigla, nomeEstado):
    self.sigla = sigla
    self.nomeEstado = nomeEstado
    self.proximo = None

  def __repr__(self):
    atual = self
    estados = []
    while atual:
      estados.append(atual.sigla)
      atual = atual.proximo
    return " -> ".join(estados)

  def posicaoPorEstado(sigla, nomeEstado):
    posicao = 0

    if sigla == "DF":
      posicao = 7
    else:
      posicao = (ord(sigla[0]) + ord(sigla[1])) % 10

    return posicao

  def inserirEstado(sigla, nomeEstado):
    posicao = EmplacamentoPorEstado.posicaoPorEstado(sigla, nomeEstado)
    novo_estado = EmplacamentoPorEstado(sigla, nomeEstado)
    novo_estado.proximo = tabela_hash[posicao]
    tabela_hash[posicao] = novo_estado

  def inserirEstadoFicticio(sigla, nomeEstado):
    posicao = EmplacamentoPorEstado.posicaoPorEstado(sigla, nomeEstado)
    novo_estado = EmplacamentoPorEstado(sigla, nomeEstado)
    novo_estado.proximo = tabela_hash[posicao]
    tabela_hash[posicao] = novo_estado


def menu():
  while True:
    print("\n", "-" * 10, "Escolha uma das opções", "-" * 10)
    print("1. Inserir estado Ficticios")
    print("2. Exibir tabela hash (completa)")
    print("3. Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
      sigla = input("Digite a sigla do estado fictício: ")
      nomeEstado = input("Digite o nome do estado fictício: ")
      EmplacamentoPorEstado.inserirEstadoFicticio(sigla, nomeEstado)
    elif opcao == 2:
      print("Exibindo a tabela hash após inserção:")
      for i in range(len(tabela_hash)):
        if tabela_hash[i] is not None:
          print(f"{i}: {tabela_hash[i]}")
        else:
          print(f"{i}:")
    elif opcao == 3:
      print("Saindo do programa...")
      break


if __name__ == "__main__":
  tabela_hash = [None] * 10

  print("Iniciando a tabela hash (vazia)...")
  for i in range(len(tabela_hash)):
    print(f"{i}: {tabela_hash[i]}")

  print("\nInserindo todos os estados brasileiros na tabela hash...")
  listaEstados = [
    ("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), ("AM", "Amazonas"),
    ("BA", "Bahia"), ("CE", "Ceará"), ("DF", "Distrito Federal"), ("ES", "Espírito Santo"),
    ("GO", "Goiás"), ("MA", "Maranhão"), ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"),
    ("MG", "Minas Gerais"), ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"),
    ("PE", "Pernambuco"), ("PI", "Piauí"), ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"),
    ("RS", "Rio Grande do Sul"), ("RO", "Rondônia"), ("RR", "Roraima"), ("SC", "Santa Catarina"),
    ("SP", "São Paulo"), ("SE", "Sergipe"), ("TO", "Tocantins"),
  ]
  
  for sigla, nomeEstado in listaEstados:
    EmplacamentoPorEstado.inserirEstado(sigla, nomeEstado)

  menu()
