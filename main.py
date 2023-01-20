from fastapi import FastAPI , File , UploadFile
from fastapi.responses import HTMLResponse, StreamingResponse
import pandas as pd

app = FastAPI(title = 'Consultas para el departamento de Análisis de Datos',
description= 'API para realizar las consultas requeridas el día 16/1/2023 sobre plataformas de streaming.',)

df = pd.read_csv('data_pi.csv')

# HOW TO USE ME

@app.get("/")  
def index():
    multi_line_string = """
Para el correcto funcionamiento de la API se debe considerar los siguiente:
* Pegar el código correspondiente a cada query a continuación de esta URL.
* Modificar el valor del parámetro introduciendo valores válidos que se encuentren en el Dataset.
* Respetar siempre la ubicación que cada parámetro como se provee en el código.
* Nunca modifique el primer bloque de texto que está entre barras /get_.../

ej: La API le devolverá la cantidad de veces que la palabra amazing está en la plataforma amazon si pega el código

/get_word_count/amazing/amazon 

Mal código -- > /get_word_count/amazon/amazing 
Mal código -- > /get_word_count/cablevision/amazing 


CODIGOS PARA LAS QUERYS

Query 1 -- > Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma.

/get_word_count/complete con la palabra que desea entontrar/complete con la plataforme que desea encontrar

Query 2 --> Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año.

/get_score_count/score/year/platform

Query 3 --> # La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.

/get_second_score/platform

Query 4 --> Película que más duró según año, plataforma y tipo de duración.

/get_longest/platform/year/duration_type

Query 5 --> Cantidad de series y películas por rating        
/get_rating_count/rating

"""
    return  print(multi_line_string)

# CODIGOS DE LAS QUERYS

# Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma.

@app.get('/get_word_count/{keyword}/{platform}')
async def get_word_count(keyword:str , platform:str):
    q1 = df[(df['title'].str.contains(keyword)) & (df['plataforma'] == platform)].shape[0]
    return  f' La palabra {keyword} aparece {q1} veces entre los títulos de la plataforma {platform}.'

# Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año.

@app.get('/get_score_count/{score}/{year}/{platform}')
async def get_score_count(score:int , year:int , platform:str):
    q2 = df[(df['plataforma'] == platform) & (df['score'] > score) & (df['release_year'] == year)].shape[0]
    return f' En la plataforma {platform} hay {q2} películas con score mayor a {score} realizadas en el año {year}.'

# La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.

@app.get('/get_second_score/{platform}')
async def get_second_score(platform:str):
    q3 = df[(df['plataforma'] == platform) & (df['type'] == 'movie' )].sort_values(by = ['score','title'] , ascending = [False , True]).iloc[1,3]
    return f' La película solicitada para la plataforma {platform} se titula {q3}.'

# Película que más duró según año, plataforma y tipo de duración.

@app.get('/get_longest/{platform}/{year}/{duration_type}')
async def get_longest(platform:str , year:int , duration_type:str):
    q4 = df[(df['plataforma'] == platform) & (df['release_year'] == year) & (df['duration_type'] == duration_type)].sort_values(by = 'duration_int' , ascending = False).iloc[0,3]
    q4_1 = df[(df['plataforma'] == platform) & (df['release_year'] == year) & (df['duration_type'] == duration_type)].sort_values(by = 'duration_int' , ascending = False).iloc[0,15]
    return f' El contenido más largo de {platform} generado en {year} se llama {q4} y dura {q4_1} {duration_type}.'

# Cantidad de series y películas por rating        
@app.get('/get_rating_count/{rating}')
async def get_rating_count(rating:str):
    q5 = df[df['rating'] == rating].shape[0]
    return f' Existen en total {q5} contenidos de un rating {rating}.'