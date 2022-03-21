[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/optimizacion-2-2022-gh-classroom/practica-1-segunda-parte-pautrejo/main) 

# **Parte 2 para la práctica 1 del curso de Optimización 2 2021-1: implementación de método numérico para resolver problemas de optimización convexa.**

# Descripción: 

Implementar un método numérico que resuelva problemas de optimización convexa de pequeña escala.

# Divisón del equipo

| User| Equipo | Tareas | Roles | 
|:---:|:---:|:---:|:---:|
| jesusmb230795| Programming| Método de pequeña escala| Programer/Reviewer |
| pautrejo| Programming, Project Manager| Documentación del paquete| Programer/Reviewer |
| joelitam2021| Programming| Docker y botón de binder| Programer/Reviewer |
| AideJGC| Programming| Test | Programer/Reviewer| 

## Trabajo: 

### Resúmen

Resolvimos los siguientes *issues* 

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


**Aide Jazmín González Cruz:** Investigación de algunas formas de evaluar el correcto funcionamiento del médtodo de Bellman Ford, elaboración de las pruebas unitarias y creaciónn del yaml para correr estos test de forma automática al hacer push sobre el proyecto.



# Descripción de archivos:

* Documentación: [Welcome to Bellman Ford Method’s documentation!](https://optimizacion-2-2022-gh-classroom.github.io/practica-1-segunda-parte-pautrejo/html/index.html)

# Comando de docker

* docker run --rm -v \<ruta a mi directorio\> :/datos --name jupyterlab_practica2 -p 8888:8888 -d joelitam2021/pkg_optimizacion:0.1
 
Después de correr la imagen de docker en su computadora, podrá acceder el jupiterlab a través de un browser mediante http://localhost:8888 

La contraseña para ingresar es qwerty


  

# Referencias:


* [Crypto Trading and Arbitrage Identification Strategies](https://nbviewer.org/github/rcroessmann/sharing_public/blob/master/arbitrage_identification.ipynb)
* [Video Dokerfile: example-docker-image-build-and-push](https://www.youtube.com/watch?v=wv7JGstFgrU&feature=youtu.be)
* [Dokerfile curso](https://github.com/palmoreck/dockerfiles/blob/master/jupyterlab/optimizacion_2/3.2.8/Dockerfile)
* [Video Get started with Binder](https://www.youtube.com/watch?v=owSGVOov9pQ)
* [ How to share a Jupyter notebook with Binder? ](https://mybinder.readthedocs.io/en/latest/introduction.html)
* [Pseudo código](https://www.simplilearn.com/tutorials/data-structure-tutorial/bellman-ford-algorithm)
