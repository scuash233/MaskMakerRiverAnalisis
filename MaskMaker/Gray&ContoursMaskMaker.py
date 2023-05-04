import cv2
import numpy as np

# Cargamos la imagen
dirImg = r"C:\Users\Public\Documents\PIV analisis\fotogramas\v2\fotogramasframe_227.jpg"
img = cv2.imread(dirImg)

# Convertimos la imagen a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplicamos un filtro Gaussiano para reducir el ruido
blur = cv2.GaussianBlur(gray, (5, 5), 0)
dirResGen = r"C:\Users\Public\Documents\PIV analisis\MaskMaker\results\gaussianBlurAplic.jpg"
cv2.imwrite(dirResGen, blur)

# Aplicamos el detector de bordes de Canny
edges = cv2.Canny(blur, 100, 200)

# Buscamos los contornos en la imagen
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Creamos una máscara vacía del mismo tamaño que la imagen original
mask = np.zeros_like(gray)

# Para cada contorno encontrado, dibujamos su región en la máscara
for contour in contours:
    cv2.drawContours(mask, [contour], 0, 255, -1)

# Aplicamos la máscara a la imagen original
result = cv2.bitwise_and(img, img, mask=mask)

# Convertimos la imagen resultante a escala de grises
result_gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

# Aplicamos un umbral para obtener una imagen binaria
_, thresh = cv2.threshold(result_gray, 10, 255, cv2.THRESH_BINARY)

# Guardamos la imagen con las partículas detectadas en una carpeta
dirRes = r"C:\Users\Public\Documents\PIV analisis\MaskMaker\results\greeGray2.jpg"
cv2.imwrite(dirRes, thresh)