
#Prog 06
import re

import os
os.system('cls')




"■■■■■■■■■■■■■■■■■■■■ Voy a eliminar esta línea >>>>>> ' ' <<<<<< Ya se Eliminó la línea desde mi PC ■■■■■■■■■■■■■■■■■■■■"----CORREGIDO






with open("D:\\Tony\\Documents\\MEGAsync\\6to Sem\\Optativa PLN - Procesamiento de Lenguaje Natural\\Programas2024\\Documentos\\archivo1.txt", 'r', encoding='utf-8') as archivo_txt:
    texto = archivo_txt.read()


expresion_regular=re.compile(r"\d+(,\d+)*(\.\d+)?")
resultados_busqueda=expresion_regular.finditer(texto)
for resultado in resultados_busqueda:
    print(resultado.group(0))
