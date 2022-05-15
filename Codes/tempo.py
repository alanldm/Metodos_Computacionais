#Bibliotecas utilizadas
import numpy as np
import time
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

                    ### CUIDADO ###
#Caso o computador utilizado tenha uma capacidade de processamento reduzida:
# - Altere o while(n!=a), por um 'a' menor
# - Aumente o valor de 'b' em n+=b no fim do while para diminuir o número de amostras
# - Faça isso para o método de Laplace e o iterativo

#----------------------------------------------------- Tempo do método de Laplace ----------------------------------------------------------
n = 9
qtdl = []
tempol = []

while(n!=189):

  timei = time.time()  

  pontos = int(((n**2) - 5*n + 6)/2)
  mpontos = np.zeros([n, n], dtype=float)  
  A = np.zeros([pontos, pontos], dtype=int)      
  b = np.zeros([pontos], dtype=int)         

  contador = 1

  for i in range (0,n):
    for j in range (0,n):
      if(i != n-1 and j != 0):            
        if(i>j):                        
          mpontos[i,j] = contador
          contador = contador + 1

  for i in range (0,n):
    for j in range (0,n):
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
        
        if(i+1!=n-1):                 
          var = int(mpontos[i+1,j])
          A[aux-1, var-1] = 1

  x = np.linalg.solve(A,b)

  timef = time.time()
  timex = timef - timei

  tempol.append(timex)
  qtdl.append(n)
  n += 9

#--------------------------------------- Tempo do Método Iterativo ----------------------------------------------------------------
chute = 0    
precisao = 0.0001     
rep = 25

n = 9
qtdr = []
tempor = []

while(n!=189):

  timei = time.time() 

  mpontos = np.zeros([n,n])                                  

  for i in range (0,n):
    for j in range (0,n):
      if(i != n-1 and j != 0):      
        if(i>j):
          mpontos[i,j] = chute    
        elif(i==j):
          mpontos[i,j] = 100      

  stop = False                    

  while((stop==False) and (rep!=0)):
    contador=0                                                                             

    for i in range (0,n):
      for j in range (0,n):
        if(i>j and i!=(n-1) and j!=0):                                                        
          aux = mpontos[i,j]                                                             
          calculo = (mpontos[i,j+1]+mpontos[i,j-1]+mpontos[i+1,j]+mpontos[i-1,j])/4        
          mpontos[i,j]=calculo                                                             
        
          erro = (calculo-aux)/calculo
          if(erro<=precisao):
            contador = contador + 1
            if(contador == ((n**2)-5*n+6)/2):
              stop = True

    rep = rep-1
  
  timef = time.time()
  timex = timef - timei

  tempor.append(timex)
  qtdr.append(n)
  n += 9

#------------------------------------------------------------------------------------------------------------------------------

#Plotando os gráficos de tempo
fig = plt.figure(figsize=(10, 10))

plt.subplot(2, 1, 1)
line1, = plt.plot(qtdl, tempol, marker='o', color='r', label="Método do Laplaciano")
line2, = plt.plot(qtdl, tempor, marker='x', color='b', label="Método iterativo")
plt.xlabel("Ordem da matriz")
plt.ylabel("Tempo de execução (s)")
plt.legend(handles=[line1, line2])
plt.title("Comparativo dos tempos de execução")
plt.xticks(qtdl)

plt.subplot(2, 2, 3)
plt.plot(qtdl, tempol, marker='o', color='r')
plt.xlabel("Ordem da matriz")
plt.ylabel("Tempo de execução (s)")
plt.title("Tempo de execução para o método de Laplace")
plt.xticks(qtdl)

plt.subplot(2, 2, 4)
line2, = plt.plot(qtdl, tempor, marker='x', color='b', label="Método iterativo")
plt.xlabel("Ordem da matriz")
plt.ylabel("Tempo de execução (ms)")
plt.title("Tempo de execução para o método iterativo")
plt.xticks(qtdl)

fig.tight_layout()
plt.savefig("Tempo.png")
plt.show()