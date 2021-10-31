import cv2
import numpy as np
from numba import njit

seed = (0, 0)


# @njit
def region_growing(image, seed=None):

    # Obter as linhas e colunas da imagem
    rows, cols = image.shape[:2]

    #  Obter o ponto de semente
    xc, yc = seed

    # Obter a cor de referência
    ref_color = image[xc, yc]

    # Criar uma matriz que conterá a região segmentada
    segmented = np.zeros_like(image)

    # Marcar o ponto de semente na imagem
    segmented[xc, yc] = ref_color

    #  Fazendo um loop pela imagem até que a região pare de crescer
    current_found = 0
    previous_points = 1

    while previous_points != current_found:

        previous_points = current_found
        current_found = 0
        for row in range(rows):
            for col in range(cols):
                # Verificar se alcançamos o ROI e pesquise na vizinhança para ver se o pixel é o mesmo
                # objeto, então, se o pixel for parte do objeto, coloque-os na imagem segmentada
                if np.array_equal(segmented[row, col], ref_color):
                    if np.array_equal(image[row - 1, col - 1], ref_color):
                        segmented[row - 1, col - 1] = ref_color
                        current_found += 1
                    if np.array_equal(image[row - 1, col], ref_color):
                        segmented[row - 1, col] = ref_color
                        current_found += 1
                    if np.array_equal(image[row - 1, col + 1], ref_color):
                        segmented[row - 1, col + 1] = ref_color
                        current_found += 1
                    if np.array_equal(image[row, col - 1], ref_color):
                        segmented[row, col - 1] = ref_color
                        current_found += 1
                    if np.array_equal(image[row, col + 1], ref_color):
                        segmented[row, col + 1] = ref_color
                        current_found += 1
                    if np.array_equal(image[row + 1, col - 1], ref_color):
                        segmented[row + 1, col - 1] = ref_color
                        current_found += 1
                    if np.array_equal(image[row + 1, col], ref_color):
                        segmented[row + 1, col] = ref_color
                        current_found += 1
                    if np.array_equal(image[row + 1, col + 1], ref_color):
                        segmented[row + 1, col + 1] = ref_color
                        current_found += 1

        cv2.imshow('Segmentation', segmented)
        cv2.waitKey(1)

    return segmented


def mouse_event(event, x, y, flags, param):
    # Verifique se o botão esquerdo está pressionado
    if event == cv2.EVENT_LBUTTONDOWN:
        global seed

        # Atualizar o ponto de semente
        seed = (y, x)


if __name__ == '__main__':
    # Ler uma imagem RGB
    image = cv2.imread('image.jpg')

    
    image = cv2.resize(image, (0, 0), fx=0.4, fy=0.4)

    # Crie uma janela, mostre a imagem original e aguarde o clique
    cv2.namedWindow('Original Image', 1)
    cv2.imshow('Original Image', image)
    cv2.setMouseCallback('Original Image', mouse_event)
    cv2.waitKey(0)

    # Aplicar o algoritmo de crescimento da região
    segmented_image = region_growing(image, seed)

    # Mostrar o resultado
    cv2.imshow('Segmented image', segmented_image)
    cv2.waitKey(0)
