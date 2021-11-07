import cv2
import numpy as np

# Ler uma imagem rgb
image = cv2.imread('image4.png')

# Transformsr para tons de cinza
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar o filtro Canny
canny_image = cv2.Canny(grayscale_image, 80, 180)

# Descubra quantos contornos existem na imagem
contours, hierarchy = cv2.findContours(canny_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Criando uma cópia da imagem para desenhar os contornos
contour_img = np.copy(image)

# Desenha todos os contornos encontrados
cv2.drawContours(contour_img, contours, -1, (0, 0, 255), 3)

#  Mostra a imagem de entrada
cv2.imshow('Input grayscale image', grayscale_image)

# Mostra os contornos encontrados
cv2.imshow('Contours', contour_img)
cv2.waitKey(0)
