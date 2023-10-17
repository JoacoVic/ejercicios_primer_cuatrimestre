from data_stark import *

while True:

    respuesta = input("A.Todos los datos de los superheroes\nB.Identidad y peso del superheroe con mayor fuerza\nC. Nombre e identidad del superheroe mas bajo\nD.Peso promedio de los superheroes masculinos\nE. Nombre y peso de los superheroes cuya fuerza supere al promedio de fuerza de los superheroes femeninos\nF.Finalizar\nElija una opcion: ")
    respuesta = respuesta.upper()


    match respuesta:
        case "A":
            for personaje in lista_personajes:
                nombre = personaje["nombre"]
                identidad = personaje["identidad"]
                empresa = personaje["empresa"]
                altura = float(personaje["altura"])
                peso = float(personaje["peso"])
                genero = personaje["genero"]
                color_ojos = personaje["color_ojos"]
                color_pelo = personaje["color_pelo"]
                fuerza = personaje["fuerza"]
                inteligencia = personaje["inteligencia"]
                print(f"nombre: {nombre} - identidad: {identidad} - empresa: {empresa} - altura: {altura:0.2f} - peso: {peso:0.2f}\ngénero = {genero} - color de ojos: {color_ojos} - color de pelo: {color_pelo} - fuerza: {fuerza} - inteligencia: {inteligencia}\n")
                
        case "B":
            mayor_fuerza = 0
            bandera_fuerza = True
            lista_mayor_fuerza = list()
            for personaje in lista_personajes:
                fuerza = int(personaje["fuerza"])
                if bandera_fuerza == True or fuerza > mayor_fuerza:
                    mayor_fuerza = fuerza
                    bandera_fuerza = False

            for personaje in lista_personajes:
                fuerza = int(personaje["fuerza"])
                identidad = personaje["identidad"]
                peso = float(personaje["peso"])
                if fuerza == mayor_fuerza:
                    print(f"\n{identidad}, cuyo peso es {peso:0.2f}, posee la mayor fuerza ({mayor_fuerza})\n")
            print(obtener_maximo(lista_personajes, "fuerza"))
        case "C":
            menor_altura = 0
            bandera_altura = True
            lista_menor_altura = list()
            for personaje in lista_personajes:
                altura = float(personaje["altura"])
                if bandera_altura == True or altura < menor_altura:
                    menor_altura = altura
                    bandera_altura = False

            for personaje in lista_personajes:
                altura = float(personaje["altura"])
                identidad = personaje["identidad"]
                nombre = personaje["nombre"]
                if altura == menor_altura:
                    print(f"\n{nombre}, cuya identidad es {identidad}, posee la menor altura ({menor_altura:0.2f})\n")

        case "D":
            acumulador_peso_masc = 0
            contador_masc = 0
            for personaje in lista_personajes:
                peso = float(personaje["peso"])
                genero = personaje["genero"]
                if genero == "M":
                    acumulador_peso_masc += peso
                    contador_masc += 1
            if contador_masc > 0:
                promedio_peso_masc = acumulador_peso_masc / contador_masc
                print(f"\nEl peso promedio de los superheroes masculinos es: {promedio_peso_masc:0.2f}\n")
            else:
                print("No hay superheroes de género masculino")

        case "E":
            acumulador_fuerza_fem = 0
            contador_fem = 0
            for personaje in lista_personajes:
                fuerza = int(personaje["fuerza"])
                genero = personaje["genero"]
                if genero == "F":
                    acumulador_fuerza_fem += fuerza
                    contador_fem += 1
            if contador_fem > 0:
                promedio_fuerza_fem = acumulador_fuerza_fem / contador_fem
                bandera_promedio = False
                for personaje in lista_personajes:
                    nombre = personaje["nombre"]
                    peso = float(personaje["peso"])
                    fuerza = int(personaje["fuerza"])
                    if fuerza > promedio_fuerza_fem:
                        bandera_promedio = True
                        print(f"\n{nombre}, cuyo peso es {peso:0.2f}, tiene una fuerza ({fuerza}) que supera el promedio de fuerza femenino {promedio_fuerza_fem:0.2f}\n")
                if bandera_promedio == False:
                    print("No hay superheroes cuya fuerza supere al promedio de fuerza de los superheroes femeninos")
            else:
                print("No hay superheroes de género femenino")
        case "F":
            break