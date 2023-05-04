import cv2

# Ruta del archivo de video
video_path = r"video\v2.mp4"

# Carpeta para guardar los fotogramas
save_folder = "fotogramas"

# Tiempo inicial y final en segundos
start_time = 2
end_time = 4

# Abre el archivo de video
cap = cv2.VideoCapture(video_path)

# Obtener el número de fotogramas por segundo
fps = cap.get(cv2.CAP_PROP_FPS)

# Saltar al fotograma inicial
start_frame = int(start_time * fps)
cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

# Obtener el fotograma actual
current_frame = start_frame

# Leer y guardar los fotogramas dentro del rango de tiempo deseado
while True:
    # Leer el fotograma actual
    ret, frame = cap.read()
    
    # Si el fotograma no se pudo leer, salir del bucle
    if not ret:
        break
    
    # Obtener el tiempo actual del fotograma
    current_time = current_frame / fps
    
    # Verificar si el fotograma está dentro del rango de tiempo deseado
    if current_time >= start_time and current_time <= end_time:
        # Guardar el fotograma en la carpeta deseada
        filename = save_folder + "frame_" + str(current_frame) + ".jpg"
        cv2.imwrite(filename, frame)
    
    # Incrementar el número de fotograma actual
    current_frame += 1
    
    # Si se alcanza el fotograma final, salir del bucle
    if current_time > end_time:
        break

# Cerrar el objeto cv2.VideoCapture
cap.release()
