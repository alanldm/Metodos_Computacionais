#Bibliotecas utilizadas
import numpy as np
import pandas as pd

mpontos = np.zeros([9,9], dtype=float)  #Matriz de pontos
A = np.zeros([21,21], dtype=int)        #Matriz de coeficientes
b = np.zeros([21], dtype=int)           #Matriz de termos independentes

contador = 1    #Contador para enumerar os pontos

#Enumerando os pontos
for i in range (0,9):
  for j in range (0,9):
    if(i != 8 and j != 0):           
      if(i>j):                        
        mpontos[i,j] = contador
        contador = contador + 1

#Montando as matrizes de coeficientes e termos independentes
for i in range (0,9):
  for j in range (0,9):
    if(mpontos[i,j]!=0):              
      aux = int(mpontos[i,j])         
      A[aux-1, aux-1] = -4            

      if(i==j+1):                     
        b[aux-1]=b[aux-1]-100
      else:                          
        var = int(mpontos[i,j+1])     
        A[aux-1, var-1] = 1

      if(j-1!=0):
        var = int(mpontos[i,j-1])
        A[aux-1, var-1] = 1

      if(j==i-1):
        b[aux-1]=b[aux-1]-100
      else:
        var = int(mpontos[i-1,j])
        A[aux-1, var-1] = 1
      
      if(i+1!=8):                 
        var = int(mpontos[i+1,j])
        A[aux-1, var-1] = 1

#Resolvendo o sistema linear e printando os resultados
x = np.linalg.solve(A,b)
print("\nPotenciais encontrados: \n")
print(x)

#Trocando a enumeração pelo valor do potencial
for i in range(0,9):
  for j in range(0,9):

      if(i==j):
        mpontos[i,j]=100                
      elif(i==8 or j==0):
        mpontos[i,j]=0                     
      elif(i>j):
        ponto = int(mpontos[i,j])   
        mpontos[i,j] = x[ponto-1]   

#Printando os resultados em um formato triangular
print("\nPotenciais em um formato triangular:")
for i in range(1,8):
  print(" ")
  for j in range(1,9):
    if(i>=j):
      print(str(round(mpontos[i,j],2)), end=" ")    

#Passando os resultados obtidos para uma tabela
df = pd.DataFrame(mpontos)
print("\n\nPotenciais tabelados: \n")
print(df)