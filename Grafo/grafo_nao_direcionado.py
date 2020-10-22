class GrafoNaoDirecionado():
  def __init__(self, vertices):
    self.vertices = vertices
    self.grafo = [[0] * vertices for i in range(vertices)]
    self.visitados = [False] * vertices

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
      adjacentes.append(soma)

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
  
  # def dfs(self, origem):
  #   self.visitados[origem - 1] = True
  #   print(self.visitados[origem - 1])
  #   print('%d visitado' % origem)
  #   for i in range(1, self.vertices + 1):
  #     if self.grafo[origem -1][i - 1] == 1 and self.visitados[i - 1] == False:
  #       self.dfs(i)
  
  def Dijkstra(self, inicio):
    distancias = [0] * 5 
    verticeAnterior = [0] * 5
    indexVetores = [0] * 5
    
    visitados = []
    pesoVisitados = []
    pesoVisitadosIndex = []

    for t in range(self.vertices):
      indexVetores[t] = t

    for i in range(self.vertices):
      distancias[i] = 999999999
    
    distancias[inicio] = 0
    verticeAnterior[inicio] = -1

    for n in range(self.vertices):
      if(n == inicio):
        continue
      if(self.grafo[inicio][n] > 0 and self.grafo[inicio][n] < distancias[n]):
        distancias[n] = self.grafo[inicio][n]
        verticeAnterior[n] = inicio
        pesoVisitados.append(self.grafo[inicio][n])
        pesoVisitadosIndex.append(n)
    
    minimoIndex = pesoVisitados.index(min(pesoVisitados))
    proximoVertice = pesoVisitadosIndex[0]
    pesoTotal = min(pesoVisitados)

    while(len(visitados) < self.vertices):
      pesoVisitados.clear()
      pesoVisitadosIndex.clear()
      visitados.append(proximoVertice)

      for n in range(self.vertices):
        pesoVisitados.clear()
        pesoVisitadosIndex.clear()

        if(visitados.__contains__(n) == True or n == proximoVertice):
          continue

        elif (self.grafo[proximoVertice][n] > 0 and self.grafo[proximoVertice][n] < distancias[n]):
          distancias[n] = self.grafo[proximoVertice][n]
          verticeAnterior[n] = proximoVertice
          pesoVisitados.append(self.grafo[proximoVertice][n])
          pesoVisitadosIndex.append(n)

        else:
          continue
      if(len(pesoVisitados) > 0):
        minimoIndex = pesoVisitados.index(min(pesoVisitados))
        pesoTotal = pesoTotal + min(pesoVisitados)
        proximoVertice = pesoVisitadosIndex[0]
        distancias[proximoVertice] = pesoTotal

    print('')
    print('Algoritmo de Menor caminho: ')
    for k in range(self.vertices):
      print(f"A menor distância do vértice {inicio} até o vértice {k} é {distancias[k]}")
    print('')
