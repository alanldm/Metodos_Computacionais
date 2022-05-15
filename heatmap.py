#Bibliotecas utilizadas
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set() #Inicializando a biblioteca seaborn

#Leitura dos dados iniciais
chute = float(input("Digite o chute inicial: "))      
precisao = float(input("Digite o valor da precisão: "))     
rep = int(input("Digite o número máximo de iterações: "))  

#Malha com 100*100 pontos
mpontos = np.zeros([100,100])                        

#Percorrendo a malha para adicionar os valores de conto e o chute inicial
for i in range (0,100):
  for j in range (0,100):
    if(i != 99 and j != 0):      
      if(i>j):
        mpontos[i,j] = chute    
      elif(i==j):
        mpontos[i,j] = 100      

#Variável de controle
stop = False                    

#Calculando iterativamente os potenciais dos pontos
while((stop==False) and (rep!=0)):
  contador=0                                                                             

  for i in range (0,100):
    for j in range (0,100):
      if(i>j and i!=99 and j!=0):                                                        
        aux = mpontos[i,j]                                                               
        calculo = (mpontos[i,j+1]+mpontos[i,j-1]+mpontos[i+1,j]+mpontos[i-1,j])/4        
        mpontos[i,j]=calculo                                                             
      
  rep = rep-1                                                                            

#Gerando uma tabela com os dados obtidos
df = pd.DataFrame(mpontos)

#Gerando o heatmap com 10000 pontos
x = sns.heatmap(df, cmap='Reds')
plt.title('Heatmap da variação da tensão')
plt.savefig("Heatmap_ordem_100.png")
plt.show()