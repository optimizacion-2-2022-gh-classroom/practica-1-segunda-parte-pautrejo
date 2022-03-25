# **Parte 2 para la práctica 1 del curso de Optimización 2 2021-1: implementación de método numérico para resolver problemas de optimización convexa.**

## Instrucciones: 

Implementar un método numérico que resuelva problemas de optimización convexa de pequeña escala. 

## Descripción: 

En está práctica se implementa el algoritmo de [Bellman Ford](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm), el cual consiste en encontrar la distancia más corta desde un nodo origen especificado, hasta todos los demás nodos del grafo, es capaz de manejar gráficos en los que algunos de los pesos de los bordes son números negativos, a diferencia del método [Dijkstra](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) que sólo trabaja con ponderaciones positivas.

## Divisón del equipo

| User| Equipo | Tareas | Roles | 
|:---:|:---:|:---:|:---:|
| jesusmb230795| Programming| Método de pequeña escala| Programer/Reviewer |
| pautrejo| Programming, Project Manager| Documentación del paquete| Programer/Reviewer |
| joelitam2021| Programming| Docker y botón de binder| Programer/Reviewer |
| AideJGC| Programming| Test | Programer/Reviewer| 

## Trabajo: 

### Resúmen

Para la presente práctica se resolvieron los siguientes *issues* 

- 1. Implementación del método numérico en Python

- 2. Crear paquete que implemente método.

- 3. Crear documentación del paquete con Sphinx

- 4. Botón de Binder para probar paquete desde repo

- 5. Dockerfile e imagen de docker

- 6. Tests método numérico
 
### Equipo
 
Nos reunimos para elegir el proyecto entre los que se habían trabajado y se seleccionó el método númerico a implementar. Así mismo, se dividieron las tareas a realizar.

### Individual

**Jesús Enrique Miranda Blanco:** Implementación del método numérico y creación del paquete que implementa el método.


**Nyrma Paulina Hernández Trejo:** Documentación del paquete realizado en Sphinx y publicado con Github Pages.


**Joel Jaramillo Pacehco:** Investigar cómo se agrega un boton de binder y su implementación en este repositorio. Creación del dockerfile y la imagen correspondiente agregando el paquete desarrollado.


**Aide Jazmín González Cruz:** Investigación de algunas formas de evaluar el correcto funcionamiento del médtodo de Bellman Ford, elaboración de las pruebas unitarias y creación del yaml para correr estos test de forma automática al hacer push sobre el proyecto. Corrida del Docker y clonar repo en AWS.


## Contenido:

### Método númerico implementado

El método de *Bellman Ford* se implemento usando python, el cuál se puede consultar en la ruta [src/bellman_ford/bellman_ford.py](https://github.com/optimizacion-2-2022-gh-classroom/practica-1-segunda-parte-pautrejo/blob/main/src/bellman_ford/bellman_ford.py). El cual ya se encuentra empaquetado y puede instalarse usando el comando:

`pip install git+https://github.com/optimizacion-2-2022-gh-classroom/practica-1-segunda-parte-pautrejo`


### Documentación

Para conocer más acerca del método implementado se creó la siguiente documentación usando el paquete de [sphinx](https://www.sphinx-doc.org/en/master/)

* [Welcome to Bellman Ford Method’s documentation!](https://optimizacion-2-2022-gh-classroom.github.io/practica-1-segunda-parte-pautrejo/html/index.html)


### Bóton binder

Se cuenta con la opción de correr el paquete usando la herramienta de *Binder*

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/optimizacion-2-2022-gh-classroom/practica-1-segunda-parte-pautrejo/main) 


### Docker

Así mismo se cuenta con una imagen de *docker* que contiene preisntalado el paquete creado para ejecutar el método de *Bellman Ford*, y el en este link se puede ver el [Dockerfile](https://github.com/optimizacion-2-2022-gh-classroom/practica-1-segunda-parte-pautrejo/blob/main/dockerfiles/pkg/Dockerfile)

Para ejecutar el *docker* se usa la siguiente instrucción:

`docker run --rm -v \<ruta a mi directorio\> :/datos --name jupyterlab_practica2 -p 8888:8888 -d joelitam2021/pkg_optimizacion:0.1`

donde **<ruta a mi directorio>** deberá sustituirse por la ruta local donde desee clonar este *docker*.
 
Después de correr la imagen de docker en su computadora, podrá acceder al *jupyterlab* a través de un *browser* usando la siguiente dirección:

`http://localhost:8888`

Le pedirá una contraseña, que por defaul es ***qwerty***.

### Tests

Se cuentan con 3 pruebas al método implementado: 2 ejemplos donde se verifica la solución correcta del método y otra que verifica que la solución no sea más grande que los nodos en el grafo, los cuales se pueden ver en el archivo [test.py][https://github.com/optimizacion-2-2022-gh-classroom/practica-1-segunda-parte-pautrejo/blob/main/test.py]. Y se ejecuta en autómatico cuando se hace un *push* en el repositorio a travéz del [test.yaml](https://github.com/optimizacion-2-2022-gh-classroom/practica-1-segunda-parte-pautrejo/blob/main/.github/workflows/test.yaml)
  

# Referencias:


* [Crypto Trading and Arbitrage Identification Strategies](https://nbviewer.org/github/rcroessmann/sharing_public/blob/master/arbitrage_identification.ipynb)
* [Video Dokerfile: example-docker-image-build-and-push](https://www.youtube.com/watch?v=wv7JGstFgrU&feature=youtu.be)
* [Dokerfile curso](https://github.com/palmoreck/dockerfiles/blob/master/jupyterlab/optimizacion_2/3.2.8/Dockerfile)
* [Video Get started with Binder](https://www.youtube.com/watch?v=owSGVOov9pQ)
* [How to share a Jupyter notebook with Binder?](https://mybinder.readthedocs.io/en/latest/introduction.html)
* [Pseudo código](https://www.simplilearn.com/tutorials/data-structure-tutorial/bellman-ford-algorithm)
* [Sphinx](https://www.sphinx-doc.org/en/master/)
* [Test case iterations Bellman Ford](https://codeforces.com/blog/entry/81979?locale=en)
