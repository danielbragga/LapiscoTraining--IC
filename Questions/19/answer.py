import cv2
import numpy as np
import matplotlib.pyplot as plt

#Ler uma imagem rgb
image = cv2.imread('arara.jpg')

# Transformar para escala de cinza
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#  Aplicar o Filtro Sobel
Gx = cv2.Sobel(grayscale_image, dx=1, dy=0, ddepth=cv2.CV_64F, ksize=3)
Gy = cv2.Sobel(grayscale_image, dx=0, dy=1, ddepth=cv2.CV_64F, ksize=3)

sobel = (Gx**2 + Gy**2)**(1/2)

# Converter para uint8
sobel = cv2.convertScaleAbs(sobel)


# Mostra os resultados
plt.figure(1)
plt.subplot(221)
plt.imshow(grayscale_image, cmap='gray')
plt.subplot(222)
plt.hist(grayscale_image.ravel(), 256, [0, 256])
plt.subplot(223)
plt.imshow(sobel, cmap='gray')
plt.subplot(224)
plt.hist(sobel.ravel(), 256, [0, 256])
plt.show()
