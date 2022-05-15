#Bibliotecas utilizadas
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set() #Inicializando o seaborn

#Leitura dos dados de entrada
chute = float(input("Digite o chute inicial: "))        
precisao = float(input("Digite o valor da precisão: "))     
rep = int(input("Digite o número máximo de iterações: "))   

#Matriz de pontos
mpontos = np.zeros([9,9])                                

#Colocando os valores de contorno e os chutes iniciais para a matriz de pontos
for i in range (0,9):
  for j in range (0,9):
    if(i != 8 and j != 0):    
      if(i>j):
        mpontos[i,j] = chute   
      elif(i==j):
        mpontos[i,j] = 100    

#Variável de controle
stop = False                 

#Calculando iterativamente
while((stop==False) and (rep!=0)):
  contador=0                                                                             

  for i in range (0,9):
    for j in range (0,9):
      if(i>j and i!=8 and j!=0):                                                       
        aux = mpontos[i,j]                                                              
        calculo = (mpontos[i,j+1]+mpontos[i,j-1]+mpontos[i+1,j]+mpontos[i-1,j])/4       
        mpontos[i,j]=calculo                                                             

        erro = abs((calculo-aux)/calculo)                                                
        if(erro<=precisao):
          contador = contador + 1                                                        
          if(contador == 21):                                                            
            stop = True
      
  rep = rep-1                                                                            

#Passandos os resultados obtidos para uma tabela
df = pd.DataFrame(mpontos)
print("\nTabela com potenciais:\n")
print(df)

#Gerando um heatmap com uma malha 9x9
x = sns.heatmap(df, cmap='Reds')
plt.title('Heatmap da variação da tensão')     
plt.savefig("Heatmap_ordem_9.png")                    
plt.show()  