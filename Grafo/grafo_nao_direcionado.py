class GrafoNaoDirecionado():
  def __init__(self, vertices):
    self.vertices = vertices
    self.grafo = [[0] * vertices for i in range(vertices)]
    self.visitados = [False] * vertices
    print(self.visitados)

  def adicionarAresta(self, origem, destino, peso):
    self.grafo[origem][destino] = peso
    self.grafo[destino][origem] = peso
  
  def printarGrafo(self):
    print('Grafo Não Direcionado: \n')
    for i in self.grafo:
      for j in i:
        print(j, end=' ')
      print('')
  
  def getAdjacentes(self):
    for i in range(self.vertices):
      print(f"Vértice {i} é adjacente a:")
      for j in range(self.vertices):
        if(self.grafo[i][j] != 0):
          print(f'{j}, ', end='')
      print('\n')
  
  def ehRegular(self):
    adjacentes = []
    primeiroElementoAux = 0
    for i in range(self.vertices):
      soma = 0
      for j in range(self.vertices):
        soma += self.grafo[i][j]

    for a in range(len(adjacentes)):
      primeiroElementoAux = adjacentes[0]
      if(adjacentes[a] != primeiroElementoAux):
        return False
    return True

  def ehCompleto(self):
      adjacencias = []

      for i in range(self.vertices):
          soma  = 0
          for j in range(self.vertices):
              soma += self.grafo[i][j]
          adjacencias.append(soma)
      
      for a in range(len(adjacencias)):
          if(adjacencias[a] != self.vertices - 1):
              return False
      return True
  
  # def ehConexo(self):
  #   def dfs(self, origem):
  #     cont = 0
  #     self.visitados[origem - 1] = True
  #     print(f'{origem} visitado')
  #     for i in range(1, self.vertices + 1):
  #       if(self.grafo[origem - 1][i - 1] == 1 and self.visitados[i - 1] == False):
  #         cont += 1
  #         self.dfs(i)
  #         print(cont)