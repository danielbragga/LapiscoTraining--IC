import cv2

#Ler uma imagem rgb
image = cv2.imread('image.jpg')

#Mostrar uma imagem rgb
cv2.imshow('Image', image)
cv2.waitKey(0)

#Salvar a imagem carregada
cv2.imwrite('saved_image.jpg', image
