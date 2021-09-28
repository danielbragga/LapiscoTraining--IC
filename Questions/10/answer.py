import cv2
import numpy as np

#ler uma imagem rgb
image = cv2.imread('car.jpg')

#transformar para tons de cinza
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#mostrar a imagem de entrada
cv2.imshow('Input grayscale image', grayscale_image)
cv2.waitKey(0)

#Obtenha as linhas e colunas da imagem
rows, cols = grayscale_image.shape[:2]

#Criar uma matriz de zeros
threshold_matrix = np.zeros((rows, cols), dtype=np.uint8)

for row in range(rows):
    for col in range(cols):
        threshold_matrix[row, col] = grayscale_image[row, col]

# Salvar todos os pixels em um arquivo txt
with open('result.txt', 'w') as outfile:
    for row in range(rows):
        for col in range(cols):
            # Define the limits of the threshold
            if threshold_matrix[row, col] < 127:
                threshold_matrix[row, col] = 0
            else:
                threshold_matrix[row, col] = 255

            outfile.write(str(threshold_matrix[row, col]) + ' ')
        outfile.write('\n')
