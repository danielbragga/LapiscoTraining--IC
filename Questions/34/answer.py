import cv2
import numpy as np

#Ler uma imagem rgb
image = cv2.imread('image4.png')

# Transformar para tons de cinza
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Criar uma cópia da imagem para desenhar os contornos
contour_img = np.copy(image)

# Excluir a variável para liberar memória
del image

# Aplique o filtro Canny
canny_image = cv2.Canny(grayscale_image, 80, 180)

# Descubrir quantos contornos existem na imagem
contours, hierarchy = cv2.findContours(canny_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#  Excluindo a variável para liberar memória
del canny_image
del hierarchy

# Encontre uma aproximação de polígono para cada contorno e, em seguida, encontre o retângulo delimitador para cada polígono
contours_poly = [None] * len(contours)
bound_rect = [None] * len(contours)

for i, contour in enumerate(contours):
    contours_poly[i] = cv2.approxPolyDP(contour, 2, True)
    bound_rect[i] = cv2.boundingRect(contours_poly[i])

# Desenhe os retângulos para cada objeto, existem dois contornos para cada objeto, porque as bordas podem ser encontradas e quando findcontours for aplicado, ele encontrará um contorno interno e um externo
for i, contour in enumerate(contours_poly):
    cv2.rectangle(contour_img, (int(bound_rect[i][0]), int(bound_rect[i][1])),
                  (int(bound_rect[i][0]) + int(bound_rect[i][2]), int(bound_rect[i][1]) + bound_rect[i][3]),
                  (255, 0, 0), 2)

    # Recortando cada objeto
    crop = contour_img[int(bound_rect[i][1]):int(bound_rect[i][1]) + bound_rect[i][3],
                       int(bound_rect[i][0]):int(bound_rect[i][0]) + int(bound_rect[i][2])]

    cv2.imshow('Object ' + str(i + 1), crop)
    cv2.waitKey(10)

    # Excluir a variável para liberar memória
    del crop

# Mostre a imagem de entrada
cv2.imshow('Input grayscale image', grayscale_image)

del grayscale_image

# Mostra os contornos encontrados
cv2.imshow('Contours', contour_img)
cv2.waitKey(0)
