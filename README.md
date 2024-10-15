# tp4-aed-utn
📄 Resumen del Trabajo
Este proyecto aborda el procesamiento eficiente de un archivo con 500 mil registros de envíos. Cada registro contiene información clave, como:
Código Postal
Dirección física
Tipo de envío
Forma de pago

Debido al gran volumen de datos, se optó por utilizar la librería Pickle para almacenar la información en un archivo binario, lo que permite una lectura y escritura más rápida en comparación con archivos de texto. El flujo principal del programa incluye:

Lectura del archivo de texto línea por línea.

Procesamiento de los datos para crear estructuras utilizables.

Guardado del conjunto de datos en un archivo binario (archivo.bin).

Este enfoque no solo facilita el manejo de datos grandes, sino que también asegura una mejor performance al cargar los datos desde un archivo.

El proyecto busca aplicar conceptos fundamentales de Algoritmos y Estructuras de Datos, como la eficiencia en el acceso a la información y la persistencia de datos.