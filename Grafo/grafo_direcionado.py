from collections import defaultdict

class GrafoDirecionado(object):

    def __init__(self, arestas, direcionado=False):
        #Estruturando o grafo
        self.adj = defaultdict(set)
        self.direcionado = direcionado
        self.adiciona_arestas(arestas)