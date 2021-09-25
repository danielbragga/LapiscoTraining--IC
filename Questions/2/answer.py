import cv2

#Ler a imagem rgb
image = cv2.imread('image.jpg')

#transformar em níveis de cinza
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#visualizar a imagem em níveis de cinza
cv2.imshow('Grayscale Image', grayscale_image)
cv2.waitKey(0)

#Salvar o resultado
cv2.imwrite('grayscale_image.jpg', grayscale_image)
