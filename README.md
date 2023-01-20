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

Finalmente se realiza el deploy de FastAPI en la Deta Cloud para disponibilizar el acceso a las querys requeridas online.


## **Video**

En el siguiente link pueden acceder a un breve resumen explicativo que se realizó a pedido del Tech Lead, el cual describe el workflow, muestra los resultados y comparte con los compañeros de Data Analytics como interactuar eficazmente con la API.