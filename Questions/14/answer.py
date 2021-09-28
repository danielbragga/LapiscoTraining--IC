import cv2

# Inicialize a câmera
cap = cv2.VideoCapture(0)

while 1:
    # Capturar cada frame
    ret, frame = cap.read()

    # Converter cada frame de bgr para cinza
    grayscale_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Mostrar o resultado
    cv2.imshow('Video', grayscale_image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
