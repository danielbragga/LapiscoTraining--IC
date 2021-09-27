import cv2

# Ler uma imagem rgb
image = cv2.imread('arara.jpg')

#transformar em tom de cinza
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Aplicar o filtro Canny (mudar os limites inferior e superior e ver a diferença)
canny_image = cv2.Canny(grayscale_image, 80, 180)

#Mostrar a imagem de entrada
cv2.imshow('Input grayscale image', grayscale_image)

#Mostra o resultado do canny filter
cv2.imshow('Canny filter result', canny_image)

cv2.waitKey(0)

#Salvar os resultados
cv2.imwrite('canny_filter_result.jpg', canny_image)
