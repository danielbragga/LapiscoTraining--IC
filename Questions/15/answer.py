import cv2

# Iniciar a camera
cap = cv2.VideoCapture(0)

while 1:
    # Capturando cada frame
    ret, frame = cap.read()

    # Converter o frame de bgr para cinza
    grayscale_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    canny = cv2.Canny(grayscale_image, 30, 100)

    # Mostrar o resultado
    cv2.imshow('Video', canny)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
