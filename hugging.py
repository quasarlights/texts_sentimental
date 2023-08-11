from transformers import pipeline
import os
from IPython.display import clear_output
import time

#@markdown # Hola 👋! Selecciona la operacion que quieres realizar 👇
Tarea = "Analisis Sentimiento" #@param ["Resumir", "Analisis Sentimiento"]

Texto = "El producto es mucho mejor que el original. Se lo siente m\xE1s firme que el que viene de f\xE1brica." #@param {type:"string"}

if Tarea == "Resumir":
   modelo = pipeline(task="summarization", model="IIC/mt5-spanish-mlsum")
   tarea_res = modelo(Texto, min_length=10, max_length=50)
elif Tarea == "Analisis Sentimiento":
    modelo = pipeline(task="text-classification", model="pysentimiento/robertuito-sentiment-analysis")
    tarea_res = modelo(Texto)
     

# Imprimir Resultado
print(tarea_res)