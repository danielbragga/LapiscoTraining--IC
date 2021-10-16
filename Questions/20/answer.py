import cv2
import numpy as np
from numba import njit


@njit
def region_growing(image, seed=None)

    # Obter as linhas e colunas da imagem
    rows, cols = image.shape[2]

    # Obter o ponto de semente
    xc, yc = seed

    # Criar uma matriz que conterá a região segmentada
    segmented = np.zeros_like(image)

    # Marcar o ponto de semente na imagem
    segmented[xc, yc] = 255

    # Fazer um loop pela imagem até que a região pare de crescer
    current_found = 0
    previous_points = 1

    while previous_points != current_found

        previous_points = current_found
        current_found = 0
        for row in range(rows)
            for col in range(cols)
                # Verificar se alcançamos o ROI e pesquise na vizinhança para ver se o pixel é o mesmo
                # objeto, então, se o pixel for parte do objeto, coloque-os na imagem segmentada
                if segmented[row, col] == 255
                    if image[row - 1, col - 1]  127
                        segmented[row - 1, col - 1] = 255
                        current_found += 1
                    if image[row - 1, col]  127
                        segmented[row - 1, col] = 255
                        current_found += 1
                    if image[row - 1, col + 1]  127
                        segmented[row - 1, col + 1] = 255
                        current_found += 1
                    if image[row, col - 1]  127
                        segmented[row, col - 1] = 255
                        current_found += 1
                    if image[row, col + 1]  127
                        segmented[row, col + 1] = 255
                        current_found += 1
                    if image[row + 1, col - 1]  127
                        segmented[row + 1, col - 1] = 255
                        current_found += 1
                    if image[row + 1, col]  127
                        segmented[row + 1, col] = 255
                        current_found += 1
                    if image[row + 1, col + 1]  127
                        segmented[row + 1, col + 1] = 255
                        current_found += 1

    return segmented


if __name__ == '__main__'
    # Leia uma imagem rgb
    image = cv2.imread('image.jpg')

    # Transformar para tons de cinza
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Aplique o algoritmo de crescimento da região
    segmented_image = region_growing(grayscale_image,
                                     seed=(int(grayscale_image.shape[0]2), int(grayscale_image.shape[1]2)))

    # mostrar o resultado
    cv2.imshow('Segmented image', segmented_image)
    cv2.waitKey(0)
