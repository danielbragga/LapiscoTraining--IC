import cv2

#Ler uma imagem rgb
image = cv2.imread('car.jpg')

#transformar em tom de cinza
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Mostrar a imagem de entrada
cv2.imshow('Input grayscale image', grayscale_image)

# Obter as linhas e colunas da imagem
rows, cols = grayscale_image.shape[:2]

# Redimensione a imagem para ficar 2 vezes maior que o tamanho original
double_sized_image = cv2.resize(grayscale_image, (2 * rows, 2 * cols))

# Redimensione a imagem para a metade de seu tamanho original
half_sized_image = cv2.resize(grayscale_image, (int(rows/2), int(cols/2)))

# Mostrar os resultados
cv2.imshow('Double sized image', double_sized_image)
cv2.imshow('Half sized image', half_sized_image)

cv2.waitKey(0)

#Salvar os resultados
cv2.imwrite('double_sized_image.jpg', double_sized_image)
cv2.imwrite('half_sized_image.jpg', half_sized_image)

