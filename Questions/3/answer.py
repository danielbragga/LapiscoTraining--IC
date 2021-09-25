import cv2

#Ler uma imagem rgb
image = cv2.imread('arara.jpg')

#Separar os canais rgb
blue_channel, green_channel, red_channel = cv2.split(image)

#Mostrar os canais individualmente

cv2.imshow('Blue Channel', blue_channel)
cv2.imshow('Green Channel', green_channel)
cv2.imshow('Red Channel', red_channel)

cv2.waitKey(0)

#Salvar os resultados
cv2.imwrite('blue_channel.jpg', blue_channel)
cv2.imwrite('green_channel.jpg', green_channel)
cv2.imwrite('red_channel.jpg', red_channel)
