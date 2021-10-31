import cv2
import numpy as np
from numba import njit


# Ler uma imagem RGB
image = cv2.imread('image3.jpg')

# Transformar para tons de cinza
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Criar uma matriz que conterá a região segmentada
segmented = np.zeros_like(grayscale_image)

seed = (0, 0)
event_count = 0


@njit
def region_growing(image, image_marked, seed=None):

    # Obter as linhas e colunas da imagem
    rows, cols = image.shape[:2]

    # Fazer um loop pela imagem até que a região pare de crescer
    current_found = 0
    previous_points = 1

    while previous_points != current_found:

        previous_points = current_found
        current_found = 0
        for row in range(rows):
            for col in range(cols):
                # Verificar se alcançamos o ROI e pesquisar na vizinhança para ver se o pixel é o mesmo
                # objeto, então, se o pixel for parte do objeto, coloque-os na imagem segmentada
                if image_marked[row, col] == 1:
                    if image[row - 1, col - 1] < 230:
                        image_marked[row - 1, col - 1] = 1
                        current_found += 1
                    if image[row - 1, col] < 230:
                        image_marked[row - 1, col] = 1
                        current_found += 1
                    if image[row - 1, col + 1] < 230:
                        image_marked[row - 1, col + 1] = 1
                        current_found += 1
                    if image[row, col - 1] < 230:
                        image_marked[row, col - 1] = 1
                        current_found += 1
                    if image[row, col + 1] < 230:
                        image_marked[row, col + 1] = 1
                        current_found += 1
                    if image[row + 1, col - 1] < 230:
                        image_marked[row + 1, col - 1] = 1
                        current_found += 1
                    if image[row + 1, col] < 230:
                        image_marked[row + 1, col] = 1
                        current_found += 1
                    if image[row + 1, col + 1] < 230:
                        image_marked[row + 1, col + 1] = 1
                        current_found += 1

                if image_marked[row, col] == 2:
                    if image[row - 1, col - 1] < 230:
                        image_marked[row - 1, col - 1] = 2
                        current_found += 1
                    if image[row - 1, col] < 230:
                        image_marked[row - 1, col] = 2
                        current_found += 1
                    if image[row - 1, col + 1] < 230:
                        image_marked[row - 1, col + 1] = 2
                        current_found += 1
                    if image[row, col - 1] < 230:
                        image_marked[row, col - 1] = 2
                        current_found += 1
                    if image[row, col + 1] < 230:
                        image_marked[row, col + 1] = 2
                        current_found += 1
                    if image[row + 1, col - 1] < 230:
                        image_marked[row + 1, col - 1] = 2
                        current_found += 1
                    if image[row + 1, col] < 230:
                        image_marked[row + 1, col] = 2
                        current_found += 1
                    if image[row + 1, col + 1] < 230:
                        image_marked[row + 1, col + 1] = 2
                        current_found += 1

                if image_marked[row, col] == 3:
                    if image[row - 1, col - 1] < 230:
                        image_marked[row - 1, col - 1] = 3
                        current_found += 1
                    if image[row - 1, col] < 230:
                        image_marked[row - 1, col] = 3
                        current_found += 1
                    if image[row - 1, col + 1] < 230:
                        image_marked[row - 1, col + 1] = 3
                        current_found += 1
                    if image[row, col - 1] < 230:
                        image_marked[row, col - 1] = 3
                        current_found += 1
                    if image[row, col + 1] < 230:
                        image_marked[row, col + 1] = 3
                        current_found += 1
                    if image[row + 1, col - 1] < 230:
                        image_marked[row + 1, col - 1] = 3
                        current_found += 1
                    if image[row + 1, col] < 230:
                        image_marked[row + 1, col] = 3
                        current_found += 1
                    if image[row + 1, col + 1] < 230:
                        image_marked[row + 1, col + 1] = 3
                        current_found += 1

    return image_marked


def mouse_event(event, x, y, flags, param):
    # Verificar se o botão esquerdo está pressionado
    if event == cv2.EVENT_LBUTTONDOWN:
        global seed
        global event_count
        global segmented

        event_count += 1

        segmented[y, x] = event_count


if __name__ == '__main__':
    # Crie uma janela, mostre a imagem original e aguarde o clique
    cv2.namedWindow('Mark object 1', 1)
    cv2.imshow('Mark object 1', grayscale_image)
    cv2.setMouseCallback('Mark object 1', mouse_event)

    cv2.waitKey(0)

    #  Aplique o algoritmo de crescimento da região
    segmented_image = region_growing(grayscale_image, segmented)

    # Criar uma imagem RGB
    rows, cols = segmented_image.shape[:2]
    new_img = np.zeros([rows, cols, 3], np.uint8)

    #  Pintar a região segmentada conforme a pergunta descreve
    new_img[np.where(segmented_image == 1)] = [0, 0, 255]
    new_img[np.where(segmented_image == 2)] = [255, 0, 0]
    new_img[np.where(segmented_image == 3)] = [0, 255, 0]


    # Mostrar os resultados
    cv2.imshow('Segmented image', new_img)
    cv2.waitKey(0)
