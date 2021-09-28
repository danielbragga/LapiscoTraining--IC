import cv2

#ler uma imagem rgb
image = cv2.imread('car.jpg')

#transformar em tom de cinza
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#mostrar a imagem de entrada
cv2.imshow('Input grayscale image', grayscale_image)
cv2.waitKey(0)

#Obter as linhas e colunas da imagem
rows, cols = grayscale_image.shape[:2]

#Salvar todos os pixels em um arquivo txt
with open('result.txt', 'w') as outfile:
    for row in range(rows):
        for col in range(cols):
            outfile.write(str(grayscale_image[row, col]) + ' ')
        outfile.write('\n')
