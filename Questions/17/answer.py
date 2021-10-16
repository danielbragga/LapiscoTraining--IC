import cv2
import numpy as np
import matplotlib.pyplot as plt

# Ler a imagem rgb
image = cv2.imread('car.jpg')

# Transformar para a escala de cinza
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Criar um vetor para conter o histograma original e outro para conter o histograma equalizado

original_hist = np.zeros([256], np.uint8)
equalized_hist = np.zeros([256], np.uint8)

# Calculando o histograma inicial
# rows, cols = grayscale_image.shape[:2]

img_flat = grayscale_image.flatten()

for pixel in img_flat:
    original_hist[pixel] += 1


# Calcula a função de distribuição cumulativa do histograma
cdf = [sum(original_hist[:i + 1]) for i in range(len(original_hist))]
cdf = np.array(cdf)

# Normaliza o cdf para estar entre 0-255
normal_cdf = ((cdf - cdf.min())*255)/(cdf.max() - cdf.min())
normal_cdf = normal_cdf.astype('uint8')


equalized_image = normal_cdf[img_flat]

equalized_image = np.reshape(equalized_image, grayscale_image.shape)

plt.figure(1)
plt.subplot(221)
plt.imshow(grayscale_image, cmap='gray')
plt.subplot(222)
plt.hist(grayscale_image.ravel(), 256, [0, 256])
plt.subplot(223)
plt.imshow(equalized_image, cmap='gray')
plt.subplot(224)
plt.hist(equalized_image.ravel(), 256, [0, 256])
plt.show()
