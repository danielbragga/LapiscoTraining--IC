import cv2
import matplotlib.pyplot as plt

# Ler uma imagem rgb
image = cv2.imread('car.jpg')

# Transformando para escala de cinza
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Equalizar a imagem
equalized_image = cv2.equalizeHist(grayscale_image)

# Calcular histogramas da imagem original e da imagem equalizada usando apenas openCV
original_hist = cv2.calcHist(grayscale_image, channels=[0], mask=None, histSize=[256], ranges=[0, 256])
equalized_hist = cv2.calcHist(equalized_image, channels=[0], mask=None, histSize=[256], ranges=[0, 256])

# Mostrar a imagem original, a imagem equalizada e seus histogramas
# Em python, podemos calcular e mostrar os histogramas usando apenas matplotlib
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
