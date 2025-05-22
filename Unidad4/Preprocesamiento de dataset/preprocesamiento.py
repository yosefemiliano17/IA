import os
import cv2
import numpy as np
import random
import csv

# Directorio base de entrada
carpeta_base = "DATASET/train"
carpeta_salida = "DATASET/train_aumentado"
os.makedirs(carpeta_salida, exist_ok=True)

# Cargar todas las rutas de imágenes y sus etiquetas
todasImagenes = []
for emocion in os.listdir(carpeta_base):
    carpeta_emocion = os.path.join(carpeta_base, emocion)
    if os.path.isdir(carpeta_emocion):
        for nombre_img in os.listdir(carpeta_emocion):
            ruta_img = os.path.join(carpeta_emocion, nombre_img)
            todasImagenes.append((ruta_img, emocion))


def ajusteBrillo(img, factor):
    return np.clip(img * factor, 0, 255).astype(np.uint8)

def rotarImagen(img, angulo):
    (h, w) = img.shape[:2]
    centro = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(centro, angulo, 1.0)
    giro = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
    return giro

with open("metadata.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["nombre_archivo", "etiqueta_emocion", "tipo_transformacion"])

    for rutaImg, emocion in random.sample(todasImagenes, min(400, len(todasImagenes))):
        img = cv2.imread(rutaImg, cv2.IMREAD_GRAYSCALE)
        if img is None:
            continue

        img_name = os.path.basename(rutaImg)

        transformaciones = [
            (img, f"original_{img_name}", "original"),
            (ajusteBrillo(img, 0.6), f"dark_{img_name}", "brillo_reducido"),
            (ajusteBrillo(img, 1.4), f"bright_{img_name}", "brillo_aumentado"),
            (rotarImagen(img, 15), f"rot15_{img_name}", "rotacion_15"),
            (rotarImagen(img, -30), f"rotneg30_{img_name}", "rotacion_-30")
        ]

        for imgTransformado, nombre, tipo in transformaciones:
            carpeta_emocion_salida = os.path.join(carpeta_salida, emocion)
            os.makedirs(carpeta_emocion_salida, exist_ok=True)
            rutaSalida = os.path.join(carpeta_emocion_salida, nombre)
            cv2.imwrite(rutaSalida, imgTransformado)
            writer.writerow([nombre, emocion, tipo])

print("Preprocesamiento terminado.")
