# pythonBasic
Nociones básicas de python

Principales características del lenguaje:

Inicio y fin de bloques de condicionales, funciones, clases y demás estructuras del lenguaje, se establecen por el identado del código. 
Aquí no existen llaves {} para indicar inicio y fin de una función, por ejemplo.
No usa el ; al final de una línea de código

Buenas prácticas:
Los nombres de los archivos van con snake case, por ejemplo: 01_nombre.py
Los nombre de las funciones van con snake case, por ejemplo: def get_name (def es palabra reservada que indica función)
Los nombre de las clases van con camel case, por ejemplo: class Person

Instalar deta (va en la ruta donde está la api que estamos desarrollando, en mi caso C:\python\backend\FastAPI ) PS C:\python\backend\FastAPI> iwr https://get.deta.dev/space-cli.ps1 -useb | iex

Después de instalar esto, en windows se hace necesario cerrar el VScode y reabrirlo para poder ejecutar 
PS C:\python\backend\FastAPI> space --help
y que muestre la lista de comandos (como comprobación de que se instaló correctamente)

El archivo requirements.txt lleva todas las dependencias, librerías, etc que deben instalarse en deta para que funcione nuestra API...

Para que podamos acceder desde VSCode y hacer pruebas en la API publica en deta, debemos agregar en el archivo Spacefile     
public: true
