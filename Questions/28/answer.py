import cv2

#  Ler uma imagem rgb
image = cv2.imread('arara.jpg')

# Transformar para tons de cinza
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar um limite adaptativo
thresholded_image = cv2.adaptiveThreshold(grayscale_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Mostrar a imagem de entrada
cv2.imshow('Input grayscale image', grayscale_image)

# Mostrar o resultado do limite adaptativo
cv2.imshow('Threshold result', thresholded_image)
cv2.waitKey(0)
