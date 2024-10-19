# Parcial-2

como ejecutar el punto 1:
 
- python3 -m venv venv                         # Crear un entorno virtual
- source venv/bin/activate                      # Activar el entorno virtual
- pip install antlr4-python3-runtime           # Instalar ANTLR Runtime
- java -jar antlr-4.x-complete.jar -Dlanguage=Python3 punto1.g4  # Compilar gramática
- python Main1.py                       # Ejecutar el main

como ejecutar el punto 2:


- java -jar antlr-4.13.0-complete.jar -Dlanguage=Python3 punto2.g4 -> generar archivos antlr
- antlr4 -Dlanguage=Python3 punto2.g4 -> compilar los archivos ant
- python Main2.py -> ejecutar el programa

 
