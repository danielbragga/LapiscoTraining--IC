import cv2
import numpy as np

# Ler uma imagem rgb
image = cv2.imread('image.jpg')

# Transformar para tons de cinza
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Mostra a imagem de entrada
cv2.imshow('Input grayscale image', grayscale_image)

# Aplicar threshold
ret, threshold_image = cv2.threshold(grayscale_image, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# Mostra o resultado do Threshold
cv2.imshow('Threshold image', threshold_image)

# Criar o elemento estruturante
kernel = np.ones((5, 5), np.uint8)

# Aplica a dilatação
for i in range(7):
    dilation = cv2.dilate(threshold_image, kernel, iterations=i)

    # Mostra o resultado da dilatação
    cv2.imshow('Dilated image', dilation)
    cv2.waitKey(1000)
