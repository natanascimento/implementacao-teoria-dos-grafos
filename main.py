#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Grafo import grafo_nao_direc

get = grafo_nao_direc.GrafoNaoDirecionado(5)

get.adicionarAresta(0, 2, 1)
get.adicionarAresta(0, 3, 1)
get.adicionarAresta(0, 4, 1)
get.adicionarAresta(1, 3, 1)
get.adicionarAresta(1, 4, 1)
get.adicionarAresta(1, 4, 1)

get.printarGrafo()