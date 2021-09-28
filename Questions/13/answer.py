import cv2
import numpy as np

#ler uma imagem rgb
image = cv2.imread('arara.jpg')

#transformar em tons de cinza
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Mostrar a imagem de entrada
cv2.imshow('Input grayscale image', grayscale_image)

#Obter as linhas e colunas da imagem
rows, cols = grayscale_image.shape[:2]

#Criar uma matriz com a mesma dimensão da imagem em tons de cinza
output_image = np.zeros((rows, cols), np.uint8)

#Aplicar convolução com o kernel Sobel
for row in range(1, rows-1):
    for col in range(1, cols-1):
        gx = grayscale_image[row - 1, col - 1] * (-1) + grayscale_image[row, col - 1] * (-2) + \
             grayscale_image[row + 1, col - 1] * (-1) + grayscale_image[row - 1, col + 1] + \
             grayscale_image[row, col + 1] * 2 + grayscale_image[row + 1, col + 1]

        gy = grayscale_image[row - 1, col - 1] * (-1) + grayscale_image[row - 1, col] * (-2) + \
             grayscale_image[row - 1, col + 1] * (-1) + grayscale_image[row + 1, col - 1] + \
             grayscale_image[row + 1, col] * 2 + grayscale_image[row - 1, col + 1]

        output_image[row, col] = (gx**2 + gy**2)**(1/2)

#Mostrar os resultados 
cv2.imshow('Sobel image', output_image)
cv2.waitKey(0)

#Salvar os resultados
cv2.imwrite('sobel_result.jpg', output_image)
