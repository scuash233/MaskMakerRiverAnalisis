import cv2
import numpy as np

# Cargamos la imagen
dirImg = r"C:\Users\Public\Documents\PIV analisis\fotogramas\v2\fotogramasframe_225.jpg"
img = cv2.imread(dirImg)

# Convertimos la imagen a HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Definimos los límites inferior y superior del rango de color verde en HSV
green_lower = np.array([0, 10, 0])
green_upper = np.array([100, 255, 255])

# Creamos una máscara de los píxeles verdes en la imagen HSV
mask = cv2.inRange(hsv, green_lower, green_upper)

# Aplicamos la máscara a la imagen original para obtener solo los píxeles verdes
green_pixels = cv2.bitwise_and(img, img, mask=mask)

# Convertimos la imagen a escala de grises
gray = cv2.cvtColor(green_pixels, cv2.COLOR_BGR2GRAY)

# Aplicamos un umbral para convertir los píxeles verdes a blanco y el fondo a negro
ret, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)

# Guardamos la imagen en una carpeta
dirRes = r"C:\Users\Public\Documents\PIV analisis\MaskMaker\results\greenMask.jpg"
cv2.imwrite(dirRes, thresh)
