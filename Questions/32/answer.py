import cv2
import numpy as np

# Ler uma imagem rgb
image = cv2.imread('image4.png')

# Transformar para tons de cinza
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicando o filtro Canny
canny_image = cv2.Canny(grayscale_image, 80, 180)

# Descubra quantos contornos existem na imagem
contours, hierarchy = cv2.findContours(canny_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print(hierarchy)

# Crie uma cópia da imagem para desenhar os contornos
contour_img = np.copy(image)

# Desenhando todos os contornos encontrados
cv2.drawContours(contour_img, contours, -1, (0, 0, 255), 3)

# Imprima a área de cada contorno, observe que existem áreas próximas a outras áreas. Portanto, pode ser considerado áreas do mesmo objeto

for i, contour in enumerate(contours):
    print('Area ' + str(i + 1) + ': ' + str(cv2.contourArea(contour)))

# Mostra a imagem de entrada
cv2.imshow('Input grayscale image', grayscale_image)

# Mostra os contornos encontrados
cv2.imshow('Contours', contour_img)
cv2.waitKey(0)
