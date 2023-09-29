import pygame
from Data_figuras import *
import math
p = math.pi

#Perimetro y area del circulo
def calcular_area_circulo(diccionario:dict)->float:
    for dimension in diccionario:
        radio = dimension["dimensiones"]
    area = p * (radio**2)
    return area

def calcular_perimetro_circulo(diccionario:dict)->float:
    for dimension in diccionario:
        radio = dimension["dimensiones"]
    perimetro = p * (radio*2)
    return perimetro



#Perimetros y areas del cuadrado y del rectángulo
def calcular_area_cuadrado_y_rectangulo(diccionario:dict)->float:
    for dimension in diccionario:
        ancho = dimension["dimensiones"][0]
        largo = dimension["dimensiones"][1]
    area = ancho * largo
    return area

def calcular_perimetro_cuadrado_y_rectangulo(diccionario:dict)->float:
    for dimension in diccionario:
        ancho = dimension["dimensiones"][0]
        largo = dimension["dimensiones"][1]
    perimetro = (ancho*2)+(largo*2)
    return perimetro

#Perimetro y area del triángulo rectángulo
def calcular_perimetro_triangulo_rectangulo(diccionario:dict, key:str)->float:
    punto_1 = diccionario[key][0]
    punto_2 = diccionario[key][1]
    punto_3 = diccionario[key][2]
    cateto_1 = punto_2[1] - punto_1[1]
    cateto_2 = punto_3[0] - punto_2[0]
    hipotenusa = ((cateto_1**2) + (cateto_2**2))**0.5
    perimetro = cateto_1 + cateto_2 + hipotenusa
    return perimetro

def calcular_area_triangulo_rectangulo(diccionario:dict, key:str)->float:
    punto_1 = diccionario[key][0]
    punto_2 = diccionario[key][1]
    punto_3 = diccionario[key][2]
    cateto_1 = punto_2[1] - punto_1[1]
    cateto_2 = punto_3[0] - punto_2[0]
    area = (cateto_1 * cateto_2)/2
    return area

print(calcular_area_triangulo_rectangulo(triangulo_rectangulo, "puntos"))

#Dibujar la figura en la ventana
def mostrar_circulo_en_ventana(diccionario:dict, pantalla, relleno=0):
    for datos in diccionario:
        radio = datos["radio"]
        posicion_inicial = datos["posicion inicial"]
        color = datos["color"]
    datos = pygame.draw.circle(pantalla,color,posicion_inicial,radio, relleno)
    return datos

def mostrar_cuadrado_y_rectangulo_en_ventana(diccionario:dict, pantalla, relleno=0):
    for datos in diccionario:
        dimensiones = datos["dimensiones"]
        posicion_inicial = datos["posicion inicial"]
        color = datos["color"]
    datos = pygame.draw.rect(pantalla,color,(posicion_inicial,dimensiones),relleno)
    return datos

def mostrar_triangulo_rectangulo_en_ventana(diccionario:dict, pantalla, relleno=0):
    for datos in diccionario:
        puntos = diccionario["puntos"]
        color = diccionario["color"]
    datos = pygame.draw.polygon(pantalla,color,puntos,relleno)
    return datos


        
