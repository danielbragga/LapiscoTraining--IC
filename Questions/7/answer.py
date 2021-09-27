import cv2

#Ler uma imagem rgb
image = cv2.imread('arara.jpg')

#  transformar em tom de cinza
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Aplicar uma limiarização (thresholding)
ret, threshold_image = cv2.threshold(grayscale_image, 70, 255, cv2.THRESH_BINARY)

#Mostrar a imagem de entrada
cv2.imshow('Input grayscale image', grayscale_image)

#Mostrar resultados
cv2.imshow('Threshold result', threshold_image)

cv2.waitKey(0)

#Salvar os resultados
cv2.imwrite('threshold_result.jpg', threshold_image)
