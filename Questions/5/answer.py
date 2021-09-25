import cv2

# Leia uma imagem rgb
image = cv2.imread('arara.jpg')

# transformar em níveis de cinza
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar os filtros de mediana e desfoque
median_image = cv2.medianBlur(grayscale_image, ksize=5)
blur_image = cv2.blur(grayscale_image, ksize=(5, 5))

# Mostra a imagem de entrada
cv2.imshow('Input grayscale image', grayscale_image)

# Mostra os resultados dos filtros de mediana e desfoque
cv2.imshow('Median filter result', median_image)
cv2.imshow('Blur filter result', blur_image)

cv2.waitKey(0)

# Salvar os resultados
cv2.imwrite('median_filter_result.jpg', median_image)
cv2.imwrite('blur_filter_result.jpg', blur_image)
