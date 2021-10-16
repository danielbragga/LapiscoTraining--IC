import cv2

# Ler uma imagem rgb
image = cv2.imread('arara.jpg')

# Transformar para escala de cinza
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicando o filtro Laplaciano
laplace = cv2.Laplacian(grayscale_image, ddepth=cv2.CV_64F, ksize=3)

# Converter para uint8
laplace = cv2.convertScaleAbs(laplace)

# Equalizando a imagem do filtro laplaciano
equalized_laplacian = cv2.equalizeHist(laplace)

# Mostra a imagem de entrada
cv2.imshow('Input grayscale image', grayscale_image)

# Mostra o resultado do filtro laplaciano
cv2.imshow('Laplacian filter result', laplace)

# Mostra o resultado da imagem equalizada do filtro laplaciano
cv2.imshow('Equalized Laplacian', equalized_laplacian)

cv2.waitKey(0)
