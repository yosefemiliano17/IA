import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import messagebox
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from nltk.corpus import stopwords

#Carga del dataset
dataset = pd.read_csv("spam_assassin.csv")

# Definir las palabras vacías (stopwords) en español e inglés para limpiar el texto
stop_words = set(stopwords.words('spanish')).union(stopwords.words('english'))

#Limpieza del dataset
dataset = dataset.drop_duplicates(subset="text").copy()
dataset["text"] = dataset["text"].str.lower()
dataset["text"] = dataset["text"].str.replace("[^a-zA-Z0-9 ]", " ")
dataset["text"] = dataset["text"].str.split()
dataset["text"] = dataset["text"].apply(lambda x: " ".join([word for word in x if word not in stop_words]))

#Separar el 80% del dataset para el entrenamiento del modelo y dejar el 20% restante para probarlo
texto_entrenamiento, texto_prueba, target_entrenamiento, target_prueba = train_test_split(dataset['text'], dataset['target'], test_size=0.20, random_state=42)

#Convertir cada correo a vectores de frecuencia en el que cada palabra se contabilizara
vectorizador = CountVectorizer()
texto_entrenamiento_count = vectorizador.fit_transform(texto_entrenamiento)
texto_prueba_count = vectorizador.transform(texto_prueba)

modelo = MultinomialNB()
modelo.fit(texto_entrenamiento_count, target_entrenamiento)

#Evaluar el modelo
resultados = modelo.predict(texto_prueba_count)
precision = np.mean(resultados == target_prueba.values)
recuperacion = np.sum((resultados == 1) & (target_prueba.values == 1)) / np.sum(target_prueba.values == 1)
print("Precision:", precision)
print("Recuperacion:", recuperacion)

#Funcion para predecir un email dado un correo obtenido por parametro
def predecir_email(email):
    email = email.lower()  
    email = email.replace("[^a-zA-Z0-9 ]", " ")
    palabras = email.split()  
    email_limpio = " ".join(word for word in palabras if word not in stop_words)  
    email_vectorizado = vectorizador.transform([email_limpio])
    prediccion = modelo.predict(email_vectorizado)[0]
    return "spam" if prediccion == 1 else "no spam"

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Detector de Spam")
ventana.geometry("400x300")

# Crear los campos de entrada
tk.Label(ventana, text="Emisor:").pack()
entrada_emisor = tk.Entry(ventana, width=50)
entrada_emisor.pack()

tk.Label(ventana, text="Receptor:").pack()
entrada_receptor = tk.Entry(ventana, width=50)
entrada_receptor.pack()

tk.Label(ventana, text="Mensaje:").pack()
entrada_mensaje = tk.Text(ventana, width=50, height=5)
entrada_mensaje.pack()

# Etiqueta de resultado
resultado_label = tk.Label(ventana, text="", font=("Arial", 12, "bold"))
resultado_label.pack(pady=10)

# Función para analizar el correo cuando se presiona el botón
def analizar_correo():
    emisor = entrada_emisor.get()
    receptor = entrada_receptor.get()
    mensaje = entrada_mensaje.get("1.0", "end-1c")
    if not emisor or not receptor or not mensaje:
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos")
        return
    email_completo = f"From: {emisor}, To: {receptor}, Message: {mensaje}"
    prediccion = predecir_email(email_completo)
    if prediccion == "spam":
        resultado_texto = f"El correo es: SPAM"
        resultado_label.config(text=resultado_texto, fg="red")
    else:
        resultado_texto = f"El correo es: NO SPAM"
        resultado_label.config(text=resultado_texto, fg="green")

# Añadir botón para analizar
boton_analizar = tk.Button(ventana, text="Analizar", command=analizar_correo)
boton_analizar.pack(pady=10)

# Iniciar el bucle principal de la interfaz
ventana.mainloop()

