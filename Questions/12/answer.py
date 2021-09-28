import cv2 
import numpy as np


#Ler o arquivo de texto
filename = 'result_10.txt'
image = []
with open(filename, 'r') as infile:
      #iterar através das linhas do arquivo de texto
      for i, line in enumerate(infile):
        # Converter cada número da linha para int
        row = [int(number) for number in line.split()]
        # Verificar se é a primeira iteração
        if i == 0:
            # Criar a primeira linha da imagem
            image = np.hstack(row)
        else:
            # Se não for a primeira iteração, adicionar novas linhas para compor a imagem
            image = np.vstack(([image, row]))


# Converter a imagem de float64 para uint8
result = np.asarray(image, np.uint8)

#Mostrar a imagem
cv2.imshow('Read image', result)
cv2.waitKey(0)






