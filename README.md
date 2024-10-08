# PG1_concurrencia

Este repositorio contiene el código de la práctica guiada "Concurrencia y 
Paralelismo" de la asignatura Software Avanzado Radar (SARA) del Master en 
Sistemas Radar.

El repositorio contiene las siguientes carpetas:
- `app`: contiene el archivo main.py para ejecutar la aplicación y la carpeta 
`src` donde se situan el resto de archivos.
- `app/src`: contiene cada uno de los paquetes de python que usaremos durante 
el desarrollo de la práctica dividido de forma básica por las diferentes 
funcionalidades.
  - `actors`: contiene las distintas clases con la lógica de funcionamiento 
  principal de la práctica
  - `helpers`: contiene archivos con funcionalidades generales del proyecto 
  que pueden ser utilizada por cualquier clase principal.
  - `base`: contine clases base utilizadas en como núcleo de distintas 
  funcionalidades del proyecto.

## Escenario de la práctica
El escenario de la práctica consiste en una implementación de un modelo 
digital de un radar. Además del modelo del radar también existe un modelo 
digital de puntos con distintas caraterísticas que pueden ser detectados por 
el radar. Estos modelos serán los actores principales y su implementación se 
puede consultar en el paquete `app/actors/*`.

Ambos modelos digitales son entidades independientes por lo que se han están 
implementados utiliando hebras permitiendo su ejecución de concurrente. Esto 
provoca que nos veamos obligados a implementar algún pratón de diseño de los 
estudiados con el objetivo de manejar los datos generados por las distintas 
detecciones del radar. El patrón que vamos a utilizar es el de "Monitor" y el 
de "Productor-Consumidor".

### Clase Radar
La clase `Radar` implementa un modelo digital del funcionamiento de un radar 
real. Esta clase hereda de `Thread` por lo que cada objeto de esta clase es 
capaz de ejecutarse como una hebra. 

Este radar tiene como atributos:
  - name: nombre del radar
  - x e y: coordenadas de la posición del radar
  - detection_range: distancia de detección del radar
  - orientation: ángulo de orientación inicial del radar
  - facing: ángulo actual del radar
  - detection: distancia a la que se detecta un objeto
  - points: objetos `Point` que el radar es capaz de detectar

Además de los anteriores atributos contiene 2 tipos de métodos principales. En 
primer lugar los métodos propios del radar que principalmente se encargan de 
las operaciones matemáticas necesarias para girar el radar y detectar si 
existe algún objeto dentro de su alcance. En segundo lugar implementa los 
métodos `run` y `stop` propios de cualquier clase que hereda de `Thread` y 
puede ejecutarse como una hebra por tanto.

### Clase Punto


## Ejecución
El primer paso para poder ejecutar la práctica y comprobar su funcionamiento 
será la creación de un entorno virtual propio del proyecto. En PyCharm es 
posible crear un entorno virtual mediante la interfaz gráfica. En caso 
necesario los comandos son los siguientes.
```
# Linux
# Crear
python3 -m venv venv
# Activar
source venv/bin/activate
# Desactivar
deactivate

# Windows
# Crear
python3 -m venv venv
# Activar
venv\Scripts\activate.bat
venv\Scripts\Activate.ps1
# Desactivar
deactivate
```

Una vez creado el entorno virtual es necesario instalar las dependencias 
propias del proyecto. Las dependencias están definidas en el fichero 
`requirements.txt`. En PyCharm se pueden instalar las dependencias mediante la 
interfaz gráfica. En caso necesario los comandos son los siguientes.
```
pip install -r requirements.txt
```

Por último tras instalar las dependencias necesarias en nuestro entorno 
virtual podemos arrancar el proceso principal de nuestro proyecto ejecutando 
el fichero `app/main.py`.
```
python3 app/main.py
```

## Objetivos a realizar
1. **Conversión resultados Radar.** El radar al detectar un objeto en su campo 
de visión es capaz de saber la distancia a la que se encuentra y la 
orientación relativa respecto a la suya original. Sin embargo, nos interesa 
conocer las coordenadas en la que este objeto se ha detectado por lo que
deberemos realizar la operación metemática adecuada para obtener sus 
coordenadas cartesianas.

2. **Implementar clase Monitor.** Como se ha descrito en el 
[escenario](#escenario-de-la-práctica) utilizaremos además del patrón de 
diseño "Producto-Consumidor" utilizaremos el patrón "Monitor" por lo que será 
necesario crear dicho monitor que sea capaz de controlar el acceso a las 
detecciones de los distintos radares.

3. **Implementar clase Lector.** Como se ha descrito en el
[escenario](#escenario-de-la-práctica) utilizaremos además del patrón de
diseño "Monitor" utilizaremos el patrón "Productor-Consumidor" por lo que será
necesario crear un consumidor o lector que utilice las detecciones generadas 
por los distintos radares.