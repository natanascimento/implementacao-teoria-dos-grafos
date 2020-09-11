class GrafoNaoDirecionado():
  def __init__(self, vertices):
    self.vertices = vertices
    self.grafo = [[0] * vertices for i in range(vertices)]

  def adicionarAresta(self, origem, destino, peso):
    self.grafo[origem][destino] = peso
    self.grafo[destino][origem] = peso
  
  def printarGrafo(self):
    print('Grafo Não Direcionado: \n')
    for i in self.grafo:
      for j in i:
        print(j, end=' ')
      print('')