import cv2
import numpy as np

# Ler uma imagem rgb
image = cv2.imread('image4.png')

# Transformar para tons de cinza
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar a transformada hough
circles = cv2.HoughCircles(grayscale_image, cv2.HOUGH_GRADIENT, 1, 30,
                           param1=150, param2=25, minRadius=0, maxRadius=0)

try:
    circles = np.uint16(np.around(circles))
except AttributeError:
    print('Nenhum círculo encontrado! Tente alterar os parâmetros.')
    exit()


# Criar uma cópia da imagem original para desenhar os círculos

# Desenhando todos os círculos encontrados
for xc, yc, radius in circles[0, :]:
    cv2.circle(circles_img, (xc, yc), radius, (0, 0, 255), 2)

# Mostra a imagem de entrada
cv2.imshow('Input grayscale image', grayscale_image)

# Mostra os círculos encontrados
cv2.imshow('Threshold result', circles_img)
cv2.waitKey(0)
