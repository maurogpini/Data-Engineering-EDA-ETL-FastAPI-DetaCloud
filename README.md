 <h1 align=center> MAURO GONZALO PINI
 <h1 align=center> HENRY LABS - DATA SCIENCE COHORTE 06
 <h1 align=center> PROYECTO INDIVIDUAL º1
  
 

## **Contexto**

El ejercicio simula un sprint semanal en un ambiente laboral en el cual el área de Analytics solicita al área de Data Engineering una serie de requerimientos específicos. 

Dichos requerimientos suponen un proceso de ETL y la disponibilización de los datos al equipo de analistas mediante la elaboración y ejecución de una API (para más detalles respecto de dichos requerimientos visite el archivo "Consigna" del repositorio).

## **Documentación y descripción del proceso**

En el repositorio se encuentran en la carpeta Datasets 4 archivos csv que contienen la información sobre la cual se realizó el proceso de ETL, el cual se encuentra detallado paso a paso y comentado en el notebook "Proceso_ETL".

![](Datasets/Blueprint%20y%20Workflow.png)

Como resultado de dicho proceso surge un solo archivo csv llamado "data_pi", el cual unifica toda la información previa, limpia y con las transformaciones solicitadas.

En el cuaderno "Cod_querys" se encuentra el código para satisfacer los requerimientos solicitados, principalmente utilizando la librería Pandas.   

Se puede ver la disponibilización de dichos datos a través de una API en el archivo "main.py", donde se crea un objeto que instancia la clase FastAPI y en ella se crean funciones que responden a las querys.

Finalmente se realiza el deploy de FastAPI en la Deta Cloud para disponibilizar el acceso a las querys requeridas online a través del endpoint que provee Deta.

## **Modo de uso de la API**

Para el correcto funcionamiento de la API se debe considerar los siguiente:

* Pegar el código correspondiente a cada query a continuación de esta URL.
* Modificar el valor del parámetro introduciendo valores válidos que se encuentren en el Dataset.
* Respetar siempre la ubicación que cada parámetro como se provee en el código.
* Nunca modifique el primer bloque de texto que está entre barras /get_.../

ej: La API le devolverá la cantidad de veces que la palabra amazing está en la plataforma amazon si pega el código

/get_word_count/amazing/amazon 
  

Mal código -- > /get_word_count/amazon/amazing   --> parámetros mal posicionados
  
Mal código -- > /get_word_count/cablevision/amazing   --> valor de parámetro inexistente


CODIGOS PARA LAS QUERYS

Query 1 -- > Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma.

/get_word_count/amazing/amazon 

Query 2 --> Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año.

/get_score_count/score/year/platform

Query 3 --> # La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.

/get_second_score/platform

Query 4 --> Película que más duró según año, plataforma y tipo de duración.

/get_longest/platform/year/duration_type

Query 5 --> Cantidad de series y películas por rating        
/get_rating_count/rating


## **Video**

En el siguiente link pueden acceder a un breve resumen explicativo que se realizó a pedido del Tech Lead, el cual describe el workflow, muestra los resultados y comparte con los compañeros de Data Analytics como interactuar eficazmente con la API.

## **Links**

Video --> 

API --> https://ypmsnf.deta.dev/
