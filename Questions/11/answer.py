import cv2 
import numpy as np


img = cv2.imread("imagem_3.jpg")

#transformando em tons de cinza
grayscale_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Mostrar a imagem de entrada
cv2.imshow('Input grayscale image', grayscale_image)

#Obter linhas e colunas da imagem
rows, cols = grayscale_image.shape[:2]

#Criar uma matriz de zeros 
new_image = np.zeros((626, 626), dtype=np.uint8)

#Copiando a imagem em tons de cinza para a nova imagem
for row in range(626):
    for col in range(626):
        new_image[row, col] = grayscale_image[row, col]    

#inicializando as coordenadas do centroide
xc = 0
yc = 0
count = 0

#Fazendo um loop pela imagem e encontrando os pontos do quadrado
for row in range(626):
    for col in range(626):
        if new_image[row, col] == 0:
            xc += row
            yc += col
            count += 1

#Calculando o ponto médio
xc = int(xc/count)
yc = int(yc/count)

#Desenho de um círculo no centroide do quadrado
cv2.circle(new_image, (xc, yc), 5, (255, 255, 255), -1)

#Mostrando o centroide
cv2.imshow('Centroid', new_image)
cv2.waitKey(0)

#Salvando os resultados
cv2.imwrite('centroid.jpg', new_image)
