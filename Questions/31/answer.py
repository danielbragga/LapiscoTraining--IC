import cv2
import numpy as np

# Ler uma imagem rgb
image = cv2.imread('image4.png')

# Transformar para tons de cinza
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar o filtro Canny
canny_image = cv2.Canny(grayscale_image, 80, 180)

# Descubra quantos contornos existem na imagem
contours, hierarchy = cv2.findContours(canny_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Encontrando uma aproximação de polígono para cada contorno e, em seguida, deve-se encontrar o retângulo delimitador para cada polígono
contours_poly = [None] * len(contours)
bound_rect = [None] * len(contours)

for i, contour in enumerate(contours):
    contours_poly[i] = cv2.approxPolyDP(contour, 2, True)
    bound_rect[i] = cv2.boundingRect(contours_poly[i])


# Criar uma cópia da imagem para desenhar os contornos
contour_img = np.copy(image)

#  Desenhar os retângulos para cada objeto
for i, contour in enumerate(contours_poly):
    cv2.rectangle(contour_img, (int(bound_rect[i][0]), int(bound_rect[i][1])),
                  (int(bound_rect[i][0]) + int(bound_rect[i][2]), int(bound_rect[i][1]) + bound_rect[i][3]),
                  (255, 0, 0), 2)

# Mostra a imagem de entrada
cv2.imshow('Input grayscale image', grayscale_image)

# Mostra os contornos encontrados
cv2.imshow('Contours', contour_img)
cv2.waitKey(0)
