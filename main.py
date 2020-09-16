#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Grafo import grafo_nao_direcionado

get = grafo_nao_direcionado.GrafoNaoDirecionado(5)

get.adicionarAresta(0, 2, 1)
get.adicionarAresta(0, 3, 1)
get.adicionarAresta(0, 4, 1)
get.adicionarAresta(1, 3, 1)
get.adicionarAresta(1, 4, 1)
get.adicionarAresta(1, 4, 1)

rodar = True
while rodar:
  print ("------------MENU---------------")
  print ("1 - Ilustrar Matriz de Adjacência")
  print ("2 - getAdjacentes")
  print ("3 - ehRegular")
  print ("4 - ehCompleto")
  print ("5 - ehConexo")
  print ("0 - Sair")
  print ("-------------------------------")
  execute = input("Informe um código: ")
  print ("-------------------------------")
  if execute == '1':
      get.printarGrafo()
      print('\n')

  elif execute == '2':
      get.getAdjacentes()
      print('\n')

  elif execute == '3':
      print(f"ehReguar: {get.ehRegular()}")
  
  elif execute == '4':
      print(f"ehCompleto: {get.ehCompleto()}")
  
  elif execute == '5':
      print(f"ehConexo: {get.ehConexo()}")
    
  elif execute == '0':
      run = False
      print("Saindo...")
      exit()