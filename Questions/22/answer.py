import cv2
import numpy as np
from numba import njit

seed = (0, 0)

@njit
def region_growing(image, seed=None):

    # Obter as linhas e colunas da imagem
    rows, cols = image.shape[:2]

    # Obter o ponto de semente
    xc, yc = seed

    # Criar uma matriz que conterá a região segmentada
    segmented = np.zeros_like(image)

    # Marcar o ponto de semente na imagem
    segmented[xc, yc] = 255

    # Fazer um loop pela imagem até que a região pare de crescer
    current_found = 0
    previous_points = 1

    while previous_points != current_found:

        previous_points = current_found
        current_found = 0
        for row in range(rows):
            for col in range(cols):
                # Verificar se alcançamos o ROI e pesquise na vizinhança para ver se o pixel é o mesmo
                # objeto, então, se o pixel for parte do objeto, coloque-os na imagem segmentada
                if segmented[row, col] == 255:
                    if image[row - 1, col - 1] < 127:
                        segmented[row - 1, col - 1] = 255
                        current_found += 1
                    if image[row - 1, col] < 127:
                        segmented[row - 1, col] = 255
                        current_found += 1
                    if image[row - 1, col + 1] < 127:
                        segmented[row - 1, col + 1] = 255
                        current_found += 1
                    if image[row, col - 1] < 127:
                        segmented[row, col - 1] = 255
                        current_found += 1
                    if image[row, col + 1] < 127:
                        segmented[row, col + 1] = 255
                        current_found += 1
                    if image[row + 1, col - 1] < 127:
                        segmented[row + 1, col - 1] = 255
                        current_found += 1
                    if image[row + 1, col] < 127:
                        segmented[row + 1, col] = 255
                        current_found += 1
                    if image[row + 1, col + 1] < 127:
                        segmented[row + 1, col + 1] = 255
                        current_found += 1

    return segmented


def mouse_event(event, x, y, flags, param):
    # Verificar se o botão esquerdo está pressionado
    if event == cv2.EVENT_LBUTTONDOWN:
        global seed

        # Atualizar o ponto de semente
        seed = (y, x)


def get_centroid(image):

    # Inicializar o centróide
    xc, yc = 0, 0

    rows, cols = image.shape[:2]
    count = 0
    # Fazer um loop pela imagem e encontre os pontos do quadrado
    for row in range(rows):
        for col in range(cols):
            if image[row, col] == 255:
                xc += row
                yc += col
                count += 1

    # Calcula o ponto médio
    xc = int(xc / count)
    yc = int(yc / count)

    return xc, yc


if __name__ == '__main__':
    # Leia uma imagem rgb
    image = cv2.imread('image.jpg')

    # Transformar para tons de cinza
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Criar uma janela, mostre a imagem original e aguarde o clique
    cv2.namedWindow('Original Image', 1)
    cv2.imshow('Original Image', grayscale_image)
    cv2.setMouseCallback('Original Image', mouse_event)
    cv2.waitKey(0)

    # Aplicar o algoritmo de crescimento da região
    segmented_image = region_growing(grayscale_image, seed)

    # Com a imagem segmentada podemos calcular o centróide
    xc, yc = get_centroid(segmented_image)

    # Criar uma imagem rgb
    rows, cols = segmented_image.shape[:2]
    new_img = np.zeros([rows, cols, 3], np.uint8)

    # Pintar a região segmentada como azul
    new_img[np.where(segmented_image == 255)] = [255, 0, 0]

    #Desenhar um círculo no centroide da região segmentada
    cv2.circle(new_img, (yc, xc), 5, (0, 255, 0), -1)

    # Mostrar os resultados
    cv2.imshow('Segmented image', new_img)
    cv2.waitKey(0)
